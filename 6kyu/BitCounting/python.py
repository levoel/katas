def count_bits(n):
    total = 0
    while n != 0:
        if n % 2 == 1:
            total += 1
        n = n // 2
    return total

# OR

def countBits(n):
    total = 0
    while n > 0:
        total += n % 2
        n >>= 1
    return total

# OR

def countBits(n):
    return bin(n).count("1")
