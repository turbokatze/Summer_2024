def compare_str(first, second):
    counter = 0
    for i, j in zip(first, second):
        if i != j:
            counter +=1
    return counter

first = 'abc';second='xyz'
print(compare_str(first,second))
