#!/usr/bin/env python3
"""Task 10"""

import pymongo


def update_topics(mongo_collection, name, topics):
    """function that changes all topics of a school document based on the name"""

    filter_ = {'name': name}
    new_data = {'$set': {'topics': topics}}
    result = mongo_collection.update_many(filter_, new_data)
