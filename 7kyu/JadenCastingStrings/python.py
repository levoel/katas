def toJadenCase(string):
    return " ".join(w.capitalize() for w in string.split())

# OR

def to_jaden_case(string):
    lst = []
    for i in string.split():
        lst.append(i.capitalize())
    return ' '.join(lst)

# OR

from string import capwords as toJadenCase