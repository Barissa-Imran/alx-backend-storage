#!/usr/bin/env python3
"""Module for Redis"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """count calls method"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper method"""
        key_name = method.__qualname__
        self._redis.incr(key_name, 0) + 1
        return method(self, *args, **kwargs)
    return wrapper


class Cache():
    """cache class"""
    def __init__(self):
        """init function"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store method"""
        generate = str(uuid.uuid4())
        self._redis.set(generate, data)
        return generate

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """the get method"""
        value = self._redis.get(key)
        return value if not fn else fn(value)

    def get_int(self, key):
        return self.get(key, int)

    def get_str(self, key):
        value = self._redis.get(key)
        return value.decode('utf-8')
