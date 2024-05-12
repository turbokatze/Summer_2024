num_1 = float(input("Введите число X: "))
num_2 = float(input("Введите число Y: "))

res_add = num_1 + num_2
res_substr = num_1 - num_2
res_mult = num_1 * num_2
res_div = num_1 / num_2
res_div_nr = num_1 // num_2

lst_1 = [res_add, res_substr, res_mult, res_div, res_div_nr]
print(lst_1, lst_1[-1])
