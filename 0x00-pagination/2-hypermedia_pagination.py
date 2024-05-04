#!/usr/bin/env python3
"""  index_range """
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """  index_range """
    start_index = page * page_size - page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ get page """
        assert isinstance(page, int) and \
            page > 0, "The page must be an integer greater than 0"
        assert isinstance(page_size, int) and \
            page_size > 0, "The page must be an integer greater than 0"
        start_idx, end_idx = index_range(page, page_size)
        return self.dataset()[start_idx:end_idx]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """ get hyper """
        dictionary = {}
        dictionary['page_size'] = len(self.get_page(page, page_size))
        dictionary['page'] = page
        dictionary['data'] = self.get_page(page, page_size)
        page_prev = page - 1 if page > 1 else None
        dictionary['next_page'] = page + 1 if dictionary['page_size'] > 0 else None
        dictionary['prev_page'] = page_prev
        dictionary['total_pages'] = len(self.get_page(page, page_size))
        return dictionary