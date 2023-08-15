#!/usr/bin/env python3
"""
Module for listing all documents in a collection
"""


def list_all(mongo_collection):
    """
    function that lists all documents in a collection
    """
    return [doc for doc in mongo_collection.find()]
