#!/usr/bin/env python3
"""  index_range """


def index_range(page: int, page_size: int) -> tuple:
    """  index_range """
    start_index = page * page_size - page_size
    end_index = start_index + page_size
    return (start_index, end_index)
