from itertools import groupby


def apd1(k):
    res = []
    for number in k:
        res.append(number + number)
    return res


a=input()
print(apd1(a))

