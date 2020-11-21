def in_array(array1, array2):
    lst = []
    array1 = list(set(array1))
    array2 = list(set(array2))
    for i in array1:
        for j in array2:
            if i in j:
                lst.append(i)
                break
    return sorted(lst)

# OR

def in_array(a1, a2):
    return sorted({sub for sub in a1 if any(sub in s for s in a2)})
