input_string = str(input('Введите целое число \n'))
res = []
for i, k in enumerate(input_string):
    res.append(k * (i + 1))
    print(i, "-", input_string.count(str(i)))
