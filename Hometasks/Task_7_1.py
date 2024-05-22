def lcm(a, b):
    if a > b:
        bn = a
    else:
        bn = b
    while True:
        if bn % a == 0 and bn % b == 0:
            lcm_num = bn
            break
        bn += 1
    return lcm_num


user_input = input('Введите натуральные числа через пробел: ')
lst1 = user_input.split()
lst1 = [int(num) for num in lst1]

a = lst1[0]
b = lst1[1]
res = lcm(a, b)

for i in range(2,len(lst1)):
    res = lcm(res, lst1[i])

print(f'НОК({lst1}): {res}')
