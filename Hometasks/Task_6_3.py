user_input = set(input('Введите символы: '))
set_cyrillic_lower, set_cyrillic_upper = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя', 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ'
set_alpha_lower, set_alpha_upper = 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
set_digit = '01234567890'
set_symbol = ".,!?/+-\±§@#$%^&*()<>=|}{'", '"', "'"
print('Вывод букв кириллицы: ', user_input.intersection(set_cyrillic_lower), user_input.intersection(set_cyrillic_upper))
print('Вывод английских букв: ', user_input.intersection(set_alpha_lower), user_input.intersection(set_alpha_upper))
print('Вывод символов: ', user_input.intersection(set_symbol))
print('Вывод арабских цифр: ', user_input.intersection(set_digit))