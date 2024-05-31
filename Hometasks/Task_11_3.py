user_input = int(input('Enter int numeral: '))

def conv_nums(number):
    m = ["", "M", "MM", "MMM"]
    c = ["", "C", "CC", "CCC", "CD", "D",
         "DC", "DCC", "DCCC", "CM "]
    x = ["", "X", "XX", "XXX", "XL", "L",
         "LX", "LXX", "LXXX", "XC"]
    i = ["", "I", "II", "III", "IV", "V",
         "VI", "VII", "VIII", "IX"]

    t1000 = m[number // 1000]
    t100 = c[(number % 1000) // 100]
    t10 = x[(number % 100) // 10]
    t1 = i[number % 10]

    intNum = (t1000 + t100 + t10 + t1)

    return intNum


if user_input > 0:
    print(conv_nums(user_input))
elif user_input == 0:
    print('error: no zeros in Roman numerals')
else:
    print('error: wrong input')