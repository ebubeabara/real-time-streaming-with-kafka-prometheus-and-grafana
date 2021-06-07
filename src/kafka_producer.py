from time import sleep
from json import dumps
from kafka import KafkaProducer

import library as library

__author__ = "Ebube Abara"
__copyright__ = "Ebube Abara"
__email__ = "ebubeabara3@gmail.com"


def main():
    """Publishes MESSAGES from PRODUCER to TOPICS"""
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                             value_serializer=lambda x: dumps(x).encode('utf-8'))

    for number in range(120):
        data = {
            'cpu_usage_percent': library.get_cpu_usage(),
            'virtual_memory_usage_percent': library.get_virtual_memory_usage(stats='percentage'),
            'virtual_memory_usage_available_bytes': library.get_virtual_memory_usage(stats='available'),
            'virtual_memory_usage_used_bytes': library.get_virtual_memory_usage(stats='used'),
            'swap_memory_usage_percent': library.get_swap_memory_usage(stats='percentage'),
            'swap_memory_usage_free_bytes': library.get_swap_memory_usage(stats='free'),
            'swap_memory_usage_used_bytes': library.get_swap_memory_usage(stats='used'),
            'modified_timestamp': library.get_metadata(stats='timestamp'),
            'computer_user': library.get_metadata(stats='user')
        }

        producer.send(topic='t1_postgres', value=data)
        producer.send(topic='t2_mongo', value=data)
        producer.flush()
        sleep(1)


if __name__ == '__main__':
    main()
