#!/usr/bin/python3
"""  class LIFOCache that inherits from BaseCaching and is a caching system"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    class LIFOCache that inherits from BaseCaching and is a caching system"""
    def __init__(self):
        """ init """
        super().__init__()

    def put(self, key, item):
        """ put method """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key = list(self.cache_data.keys())[-1]
                print(f'DISCARD: {last_key}')
                del self.cache_data[last_key]
            self.cache_data[key] = item

    def get(self, key):
        """ Get method """

        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
