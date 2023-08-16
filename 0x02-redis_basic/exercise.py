#!/usr/bin/env python3
"""Module for Redis"""
import redis
import uuid
from typing import Union, Callable, Optional

class Cache():
    """cache class"""
    def __init__(self):
        """init function"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union(str, bytes, int, float)) -> str:
        """store method"""
        generate = str(uuid.uuid4())
        self._redis.set(generate, data)
        return generate
