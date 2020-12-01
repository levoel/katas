def comp(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False

# OR

def comp(array1, array2):
    return False if array1 == None or array2 == None else sorted(i**2 for i in array1) == sorted(array2)
