#!/usr/bin/env python3
"""Task 8"""

import pymongo

def list_all(mongo_collection):
    """function that lists all documents in a collection"""
    collection = mongo_collection.find()
    list = []
    for fi in collection:
        list.append(fi)
    return list