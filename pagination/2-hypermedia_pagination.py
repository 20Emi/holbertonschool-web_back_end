#!/usr/bin/env python3
"""Task 2"""

#!/usr/bin/env python3
"""Task 1"""




import csv
import math
from typing import List
import math
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
        """
        Use assert to verify that both arguments are integers greater than 0.
        page1[0]:represents the start index of the range.
        page1[1]: represents the end index of the range.
        """
        assert isinstance(page, int)
        assert page > 0
        assert isinstance(page_size, int)
        assert page_size > 0
        page1 = index_range(page, page_size)
        first = page1[0]
        end = page1[1]
        return self.dataset()[first:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Implement a get_hyper method that takes the same arguments
        (and defaults) as get_page and returns a dictionary containing
        the following key-value pairs:"""

        #  the dataset page (equivalent to return from previous task)
        data = self.get_page(page, page_size)

        #  the length of the returned dataset page
        page_size = len(data)

        # the total number of pages in the dataset as an integer
        total_pages = math.ceil(page_size / len(self.dataset()))
        #  number of the next page, None if no next page
        if page > total_pages:
            next_page = None
        else:
            next_page = page + 1

        # number of the previous page, None if no previous page
        if page > 1:
            prev_page = page - 1
        else:
            prev_page = None

        # result dictionary
        result = {
            'page_size': page_size,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
        return result


def index_range(page, page_size) -> tuple:
    """
    page: The page number you want to view (starting with 1).
    page_size: The number of tuples per page.
    """
    first = (page - 1) * page_size
    end = first + page_size
    return first, end
