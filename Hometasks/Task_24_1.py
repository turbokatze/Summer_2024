def sort1(lst):
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst


lst1 = list(input().split(' '))
print(sort1(lst1))


