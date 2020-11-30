def one_two_three():
    res = one_two(), one_two()
    return ( 1 if res == (1, 1) else
             2 if res == (1, 2) else
             3 if res == (2, 1) else
             one_two_three() )
