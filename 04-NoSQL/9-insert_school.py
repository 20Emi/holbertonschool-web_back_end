#!/usr/bin/env python3
"""Task 9"""

import pymongo


def insert_school(mongo_collection, **kwargs):
    """function that inserts a new document in a collection"""

    collection = mongo_collection.insert_one(kwargs)
    return collection.inserted_id
