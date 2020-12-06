def ip_to_int32(ip):
    lst = ip.split('.')

    return sum([int(lst[-1-i]) * (2 ** (i * 8)) for i in range(len(lst))])

# OR

def ip_to_int32(ip):
    addr = ip.split(".")

    res = int(addr[0]) << 24
    res += int(addr[1]) << 16
    res += int(addr[2]) << 8
    res += int(addr[3])

    return res
