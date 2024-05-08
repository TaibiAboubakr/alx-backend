#!/usr/bin/python3
"""  class BasicCache that inherits from BaseCaching and is a caching system"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    class BasicCache that inherits from BaseCaching and is a caching system"""

    def put(self, key, item):
        """ put method """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Get method """

        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
