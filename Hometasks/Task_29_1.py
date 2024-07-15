def imposter(lst1):
    for x in lst1:
        while x == x in lst1:
            lst1.remove(x)
    return lst1

lst1 = [10, 10, 10, 10, 55]
print(imposter(lst1))