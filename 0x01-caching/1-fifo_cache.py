#!/usr/bin/python3
"""  class FIFOCache that inherits from BaseCaching and is a caching system"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    class FIFOCache that inherits from BaseCaching and is a caching system"""
    def __init__(self):
        """ init """
        super().__init__()

    def put(self, key, item):
        """ put method """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_key = next(iter(self.cache_data))
                print(f'DISCARD: {first_key}')
                del self.cache_data[first_key]
            self.cache_data[key] = item

    def get(self, key):
        """ Get method """

        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
