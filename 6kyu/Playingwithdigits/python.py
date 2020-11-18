def dig_pow(n, p):
    t = sum(int(d) ** (p+i) for i, d in enumerate(str(n)))

    return t//n if t % n == 0 else -1

# OR


def dig_pow(n, p):
    dp = 0
    for i in range(len(str(n))):
        dp += int(str(n)[i]) ** (p + i)

    return int(dp / n) if dp % n == 0 else -1

# OR


def dig_pow(n, p):
    dp = 0
    str_n = str(n)
    n = len(str_n)

    for i in range(n):
        dp += int(str_n[i]) ** (p + i)

    if dp % n == 0:
        result = dp // n
    else:
        result = -1

    return result
