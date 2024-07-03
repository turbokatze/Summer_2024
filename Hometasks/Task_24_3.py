def skobki(n):
    c,l = 0, len(n)
    if n[0] == '(' and n[-1] == ')':
        for j in range(l):
            for i in n:
                if i == '(':
                    c += 1
                elif i == ')':
                    c -= 1
    else:
        c = 100

    if c == 0:
        return True
    else:
        return False


n = list(input('Введите скобки: '))
print(skobki(n))