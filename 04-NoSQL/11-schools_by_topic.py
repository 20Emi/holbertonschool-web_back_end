#!/usr/bin/env python3
"""Task 11"""

import pymongo


def schools_by_topic(mongo_collection, topic):
    """function that returns the list of school having a speciific topic"""

    collection = mongo_collection.find({'topics': topic})
    list = []
    for fi in collection:
        list.append(fi)
    return list
