from json import loads
from psycopg2 import connect
from kafka import KafkaConsumer

__author__ = "Ebube Abara"
__copyright__ = "Ebube Abara"
__email__ = "ebubeabara3@gmail.com"


def main():
    """Subscribes to MESSAGES in TOPIC and loads them into PostgreSQL Database CONSUMER"""
    consumer = KafkaConsumer('t1_postgres',
                             bootstrap_servers=['localhost:9092'],
                             auto_offset_reset='earliest',
                             enable_auto_commit=True,
                             group_id='my-group',
                             value_deserializer=lambda x: loads(x.decode('utf-8')))

    connection, cursor = init_postgresql_connection()
    for message in consumer:
        message = message.value
        insert_into_table(cursor=cursor, schema='cpu_usage', table='kafka_consumer', message=message)
        print('{} added to {}'.format(message, 'cpu_usage.kafka_consumer table in PostgreSQL Database'))
    connection.close()
    cursor.close()


def init_postgresql_connection():
    """Initialise PostgreSQL DB connection"""
    connection = connect(user='test',
                         password='test',
                         host='localhost',
                         port='5432',
                         database='infrastructure')
    cursor = connection.cursor()
    return connection, cursor


def insert_into_table(cursor, schema, table, message):
    """SQL DML Insert kafka messages from Postgres kafka topic into kafka consumer database"""
    query = f'''
        INSERT INTO
            {schema}.{table}(
                "cpu_usage_percent", 
                "virtual_memory_usage_percent", 
                "virtual_memory_usage_available_bytes", 
                "virtual_memory_usage_used_bytes", 
                "swap_memory_usage_percent", 
                "swap_memory_usage_free_bytes", 
                "swap_memory_usage_used_bytes",
                "modified_timestamp", 
                "computer_user"
            )           
        VALUES 
            (%s, %s, %s, %s, %s, %s, %s, %s, %s);
        COMMIT;
    '''
    cursor.execute(query,
                   (
                       message['cpu_usage_percent'],
                       message['virtual_memory_usage_percent'],
                       message['virtual_memory_usage_available_bytes'],
                       message['virtual_memory_usage_used_bytes'],
                       message['swap_memory_usage_percent'],
                       message['swap_memory_usage_free_bytes'],
                       message['swap_memory_usage_used_bytes'],
                       message['modified_timestamp'],
                       message['computer_user']
                   ),)


if __name__ == '__main__':
    main()
