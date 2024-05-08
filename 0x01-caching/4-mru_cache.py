#!/usr/bin/env python3
""" class MRUCache that inherits from BaseCaching and is a caching system
"""
from collections import OrderedDict

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ class MRUCache that inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """put an item .
        """
        if key and item:
            if key not in self.cache_data:
                if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                    lru_key, _ = self.cache_data.popitem(True)
                    print("DISCARD:", lru_key)
                self.cache_data[key] = item
                self.cache_data.move_to_end(key)
            else:
                self.cache_data[key] = item

    def get(self, key):
        """Get method """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key)
        return self.cache_data.get(key, None)
