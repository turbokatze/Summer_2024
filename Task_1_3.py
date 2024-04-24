num_1 = float(input("Введите число X: "))
num_2 = float(input("Введите число Y: "))

res_add = num_1 + num_2
res_substr = num_1 - num_2
res_mult = num_1 * num_2
res_div = num_1 / num_2
res_div_nr = num_1 // num_2

if res_add >= res_substr and res_add >= res_mult and res_add >= res_div and res_add >= res_div_nr:
    print(1, res_add)
elif res_substr >= res_add and res_substr >= res_mult and res_substr >= res_div and res_substr >= res_div_nr:
    print(2, res_substr)
elif res_mult >= res_add and res_mult >= res_substr and res_mult >= res_div and res_mult >= res_div_nr:
    print(3, res_mult)
elif res_div >= res_add and res_div >= res_substr and res_div >= res_mult and res_div >= res_div_nr:
    print(4, res_div)
else:
    print(5, res_div_nr)
