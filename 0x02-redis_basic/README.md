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
