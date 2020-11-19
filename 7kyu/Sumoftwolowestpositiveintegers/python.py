def sum_two_smallest_numbers(numbers):
    a = numbers[0]
    b = numbers[1]
    num = 0
    for i in range(2, len(numbers)):
        if a > b:
            a, b = b, a
        num = numbers[i]
        if b > num:
            b = num
    return a + b

# OR

def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]

# OR

def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])
