from json import loads
from pymongo import MongoClient
from kafka import KafkaConsumer

__author__ = "Ebube Abara"
__copyright__ = "Ebube Abara"
__email__ = "ebubeabara3@gmail.com"


def main():
    """Subscribes to MESSAGES in TOPIC and loads them into MongoDB Database CONSUMER"""
    consumer = KafkaConsumer('t2_mongo',
                             bootstrap_servers=['localhost:9092'],
                             auto_offset_reset='earliest',
                             enable_auto_commit=True,
                             group_id='my-group',
                             value_deserializer=lambda x: loads(x.decode('utf-8')))

    client = MongoClient('localhost:27017')
    collection = client.infrastructure_cpu_usage.kafka_consumer

    for message in consumer:
        message = message.value
        collection.insert_one(message)
        print('{} added to {}'.format(message, collection))


if __name__ == '__main__':
    main()