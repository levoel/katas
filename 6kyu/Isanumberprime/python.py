import random


def even_odd(n):
    s, d = 0, n
    while d % 2 == 0:
        s += 1
        d >>= 1
    return s, d


def Miller_Rabin(a, p):
    s, d = even_odd(p - 1)
    a = pow(a, d, p)
    if a == 1: return True
    for i in range(s):
        if a == p - 1: return True
        a = pow(a, 2, p)
    return False


def is_prime(num):
    if num == 2: return True
    if num <= 1 or num % 2 == 0: return False
    return all(Miller_Rabin(random.randint(2, num-1), num) for i in range(40))

# OR

from itertools import count, islice

def is_prime(num):
    return num > 1 and all(num % i for i in islice(count(2), int(num ** 0.5 - 1)))
