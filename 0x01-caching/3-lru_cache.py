#!/usr/bin/python3
"""  class LRUCache that inherits from BaseCaching and is a caching system"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    array = []
    """
    class LRUCache that inherits from BaseCaching and is a caching system"""
    def __init__(self):
        """ init """
        super().__init__()

    def put(self, key, item):
        """ put method """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                                   and key not in self.cache_data:
                lru_key = self.get_delete_LRU()
                print(f"DISCARD: {lru_key}")
                del self.cache_data[lru_key]
            self.add_key(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Get method """
        if key and key in self.cache_data:
            self.add_key(key)
            return self.cache_data[key]
        return None

    def add_key(self, key):
        """ add key """
        if key in self.array:
            self.array.remove(key)
        self.array.append(key)

    def get_delete_LRU(self):
        """ retrievs and delete lru key """
        lru_key = self.array[0]
        self.array.remove(lru_key)
        return lru_key
