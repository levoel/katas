def array_diff(a, b):
    return filter(lambda element: element not in b, a)

# OR

def array_diff(a, b):
    return [element for element in a if element not in b]