#!/usr/bin/env python3
"""Task 1"""

import csv
import math
from typing import List


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

        assert isinstance(page, int)
        assert page > 0
        assert isinstance(page_size, int)
        assert page_size > 0
        page1 = index_range(page, page_size)
        first = page1[0]
        end = page1[1]
        return self.dataset()[first:end]


def index_range(page, page_size) -> tuple:
    """
    page: The page number you want to view (starting with 1).
    page_size: The number of tuples per page.
    """
    first = (page - 1) * page_size
    end = first + page_size
    return first, end
