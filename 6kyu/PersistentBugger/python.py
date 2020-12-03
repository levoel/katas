def persistence(n):
    if n < 10:
        return 0

    mult = 1
    while(n > 0):
        mult = n%10 * mult
        n = n//10

    return persistence(mult) + 1

# OR

def persistence(n):
    import operator

    i = 0
    while n >= 10:
        n = reduce(operator.mul, [int(x) for x in str(n)], 1)
        i += 1

    return i
