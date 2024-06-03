import itertools

def apd1(k):
    res = []
    for number in k:
        res.append(number + number)
    return res


# a=input()
# print(apd1(a))

def apd2(number):
    return number, number if number !=0 else number + number



for i in range(10):
    print(apd2(i), end=' ')