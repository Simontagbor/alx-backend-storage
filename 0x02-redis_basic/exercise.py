#!/usr/bin/env python3
"""
This module creates a Cache class and stores data in Redis
Cache class:
    - store(): takes a data argument and returns a string
"""
import uuid
import redis
from typing import Optional, Callable
from functools import wraps


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

    def get(self, key: str, fn: Optional[Callable] = None) -> bytes:
        """ Get the data from Redis """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def count_calls(method: Callable) -> Callable:
        """ Count the number of times a method is called """
        key = method.__qualname__
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            """ Wrapper function """
            self._redis.incr(key)
            return method(self, *args, **kwargs)
        return wrapper

    def call_history(method: Callable) -> Callable:
        """ Store the history of inputs and outputs """
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            """ Wrapper function """
            input = str(args)
            self._redis.rpush(method.__qualname__ + ":inputs", input)
            output = str(method(self, *args, **kwargs))
            self._redis.rpush(method.__qualname__ + ":outputs", output)
            return output
        return wrapper

    @call_history
    @count_calls
    def store(self, data: bytes) -> str:
        """ Generate a random key """
        key = str(uuid.uuid4())
        """ Store the input data in Redis using the random key """
        self._redis.set(key, data)
        return key


def replay(method: Callable) -> None:
    """ Display the history of calls of a particular function """
    r = redis.Redis()
    key = method.__qualname__
    count = r.get(key).decode("utf-8")
    inputs = r.lrange(key + ":inputs", 0, -1)
    outputs = r.lrange(key + ":outputs", 0, -1)
    print("{} was called {} times:".format(key, count))
    for i, o in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(key, i.decode("utf-8"),
                                 o.decode("utf-8")))
