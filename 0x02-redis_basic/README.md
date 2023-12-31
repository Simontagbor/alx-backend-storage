# 0x02. Redis basic
`Back-end` `Redis`

## Learning Outcomes
- I learned about Redis and how to use it as a caching system.
- I learned how to use Redis commands with `redis` and `redis-py` clients.
- I learned how to use `python` to manage my Redis database.
- I learned how to use `redis` for basic operations, caching, and storing simple key-value pairs.


## Tasks

### [0. Writing strings to Redis](./exercise.py)
I implemented a Class `Cache` that takes no arguments and has the following methods:
- `store`: takes a data argument and returns a string.
- `get`: takes a key string argument and returns a value.

#### Output
```
simontagbor@ubuntu:~/0x02$ cat main.py
#!/usr/bin/env python3
""" Main file"""
import redis

Cache = __import__('exercise').Cache

cache = Cache()

data = b"hello"
key = cache.store(data)
print(key)

local_redis = redis.Redis()
print(local_redis.get(key))

simontagbor@ubuntu:~/0x02$ ./main.py
3a3e8231-b2f6-450d-8b0e-0f38f16e8ca2
b'hello'
simontagbor@ubuntu:~/0x02$
```
### [1. Reading from Redis and recovering original type](./exercise.py)
I updated the class `Cache` by adding the method `get_str` that takes a `key` string argument and returns the right data.

### [2. Incrementing values](./exercise.py)
I updated the class `Cache` by adding the method `count_calls` that returns the number of times a method is called.

### [3. Storing lists](./exercise.py)
I updated the class `Cache` by adding the methods `add` and `get_list` to append strings to a list and return the list of strings stored in a list.

### [4. Retrieving lists](./exercise.py)
I updated the class `Cache` by adding the methods `get`, `get_int`, and `get_str` to return the list of strings stored in a list.

