number_1 = int(input("Введите число X: "))
number_2 = int(input("Введите число Y: "))

largest_number_add = number_1 + number_2
largest_number_substr = number_1 - number_2
largest_number_mult = number_1 * number_2
largest_number_div = number_1 / number_2

list_1 = [largest_number_add, largest_number_substr, largest_number_mult, largest_number_div]
sorted_list = sorted(list_1)
result = sorted_list[-1]
print("Наибольшее число: ", result)