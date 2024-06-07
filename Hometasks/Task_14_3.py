def tri_2n(n):
    if n == 1:
        print('*')
        return '*'
    else:
        x = n*tri_2n(n - 1)
        print(x)
        return '*'

print('Enter number: ')
print((tri_2n(int(input()))))
