user_input = input('Введите цепочку ДНК: ')
dct1 = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'T',
}
for i in user_input:
    if i not in "ACGT":
        print('Ошибка ввода')
        break
else:
    print('Цепочка РНК:', ''.join(dct1[letter] for letter in user_input))
