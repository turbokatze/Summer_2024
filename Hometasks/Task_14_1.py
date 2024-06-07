def digit_sum(n):
    if n <= 0:
        return 0
    else:
        x = n % 10
        return x % 10 + digit_sum(n // 10)

    # для отрицательных чисел:
      # x = abs(n) % 10
      # return x % 10 + digit_sum(abs(n) // 10)
print('Enter int number: ')
print(f'Digits sum: {digit_sum(int(input()))}')