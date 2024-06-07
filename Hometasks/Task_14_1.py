class OnlyLetters(ValueError): pass
def digits_len(n):
    if n <= 0:
        return 0
    else:
        x = n % 10
        return x % 10

    # для отрицательных чисел:
      # x = abs(n) % 10
      # return x % 10


try:
    user_input = input('Enter int number: ')
    if user_input.isalpha():
        raise OnlyLetters

except OnlyLetters:
    print('Input error, enter integer number')

else:
    print(f'Digits length: {digits_len(int(user_input))}')
