num_1 = float(input("Введите число X: "))
num_2 = float(input("Введите число Y: "))

res_add = num_1 + num_2
res_substr = num_1 - num_2
res_mult = num_1 * num_2
res_div = num_1 / num_2

if res_add > res_substr > res_mult > res_div:
    print(res_add)
elif res_substr > res_add > res_mult > res_div:
    print(res_substr)
elif res_mult > res_add > res_substr > res_div:
    print(res_mult)
else:
    print(res_div)