#!/usr/bin/env python3
"""Task 0"""


def index_range(page, page_size) -> tuple:
    """
    page: The page number you want to view (starting with 1).
    page_size: The number of tuples per page.
    """
    first = (page - 1) * page_size
    end = first + page_size
    return first, end
