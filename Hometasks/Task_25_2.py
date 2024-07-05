# def is_palindrome(n): return n == n[::-1] #крутой метод
# print(is_palindrome(input('Ввод: ')))


def is_palindrome(n):
    if len(n) == 0 or len(n) == 1:
        return True
    else:
        if len(n) >= 2 and n[0] == n[-1]:
            n = n[1:-1]
            res = is_palindrome(n)
            if res:
                return True
            else:
                return False
        else:
            return False

print(is_palindrome(input('Ввод: ')))