def grow(arr):


    return arr == [] or arr[0] * grow(arr[1:])
