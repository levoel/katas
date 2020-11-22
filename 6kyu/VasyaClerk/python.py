def tickets(people):
    if people[0] != 25:
        return 'NO'
    price = 25
    d ={}
    d[25] = 1
    d[50] = 0
    d[100] =0
    for i in range(len(people) - 1):
        if people[i + 1] == 25:
            d[25] = d[25] + 1
        elif people[i+1] == 50:
            if d.get(25) == 0:
                return "NO"
            else:
                d[25] = d[25] - 1
                d[50] = d[50] + 1
        elif people[i+1] == 100:
            if d.get(50) != 0 and d.get(25) != 0:
                d[50] = d[50] - 1
                d[25] = d[25] - 1
                d[100] = d[100] + 1
            elif d.get(50) == 0 and d.get(25) >= 3:
                d[25] = d[25] - 3
                d[100] = d[100] + 1
            else:
                return "NO"
    return "YES"

# OR

def tickets(people):
  till = {100:0,
          50:0,
          25:0}

  for paid in people:
    till[paid] += 1
    change = paid - 25

    for bill in (50, 25):
      while (bill <= change and till[bill] > 0):
        till[bill] -= 1
        change -= bill

    if change != 0:
      return 'NO'

  return 'YES'
