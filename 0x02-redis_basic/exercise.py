#!/usr/bin/env python3
"""
This module creates a Cache class and stores data in Redis
Cache class:
    - store(): takes a data argument and returns a string
"""
import uuid
import redis


class Cache:
    """
    Cache class to store data in-memory using Redis.

    Attributes:
        - _redis: private instance of the Redis client
    Methods:
        - store(): takes a data argument and returns a string

    Usage:
        >>> cache = Cache()
        >>> key = cache.store(b"Hello World")
        >>> print(cache._redis.get(key))
        b'Hello World'
    """
    def __init__(self):
        """ Constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: bytes) -> str:
        """ Generate a random key """
        key = str(uuid.uuid4())
        """ Store the input data in Redis using the random key """
        self._redis.set(key, data)
        return key
