import psutil
from json import dumps
from datetime import datetime

__author__ = "Ebube Abara"
__copyright__ = "Ebube Abara"
__email__ = "ebubeabara3@gmail.com"


def get_cpu_usage():
    """returns CPU usage in percentage (%)"""
    return psutil.cpu_percent()


def get_virtual_memory_usage(stats):
    """returns virtual memory usage in percentage (%), available memory in bytes or used memory in bytes"""
    if stats == 'percentage':
        return psutil.virtual_memory()[2]
    elif stats == 'available':
        return psutil.virtual_memory()[1]
    elif stats == 'used':
        return psutil.virtual_memory()[3]


def get_swap_memory_usage(stats):
    """returns swap memory usage in percentage (%), free memory in bytes or used memory in bytes"""
    if stats == 'percentage':
        return psutil.swap_memory()[3]
    elif stats == 'free':
        return psutil.swap_memory()[2]
    elif stats == 'used':
        return psutil.swap_memory()[1]


def get_metadata(stats):
    """returns metadata such as current timestamp and user"""
    if stats == 'timestamp':
        return dumps(datetime.now(), default=converter)[1:-1]
    elif stats == 'user':
        return 'Tester'


def converter(obj):
    """returns a serializable version obj (i.e. Object) or raises a TypeError Exception"""
    if isinstance(obj, datetime):
        return obj.__str__()
