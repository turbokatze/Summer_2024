def strings_compare(first,second):
    differ = 0
    if len(first) - len(second) in range(-1, 2):
        if len(first) > len(second):
            lmax = first
        else:
            lmax = second
        for i in range(len(lmax)):
            if first[i] != second[i]:
                differ += 1
        if differ <= 1:
            return True
        else:
            return False
    return False

first_string = input('Введите первую строку: ')
second_string = input('Введите вторую строку: ')
print(strings_compare(first_string, second_string))