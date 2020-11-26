def memoized(func):
    cache = {}
    def wrapped(k):
        v = cache.get(k)
        if v is None:
            v = cache[k] = func(k)
        return v
    return wrapped

@memoized
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# OR

from functools import lru_cache

@lru_cache()
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
