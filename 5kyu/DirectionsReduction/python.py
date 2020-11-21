def dirReduc(arr):
    new_arr = []
    for i in arr:
        new_arr.append(i)
        while set(new_arr[-2:]) == set(['NORTH','SOUTH']) or set(new_arr[-2:]) == set(['WEST','EAST']):
            new_arr[-2:] = []
    return new_arr

# OR

def dirReduc(arr):
    new_arr = []
    for d in arr:
        if new_arr and new_arr[-1] == opposite[d]:
            new_arr.pop()
        else:
            new_arr.append(d)
    return new_arr
