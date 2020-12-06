def int32_to_ip(int32):
    return '{}.{}.{}.{}'.format(*int32.to_bytes(4, 'big'))

# OR

from ipaddress import IPv4Address

def int32_to_ip(int32):
    return str(IPv4Address(int32))
