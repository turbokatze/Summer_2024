def lc_deco(func):
    def wrapper():
        res_func = func()
        lc_res = res_func.lower()
        return lc_res
    return wrapper


def user_input():
    s = input('Ввод: ')
    return s


res = lc_deco(user_input)
print(f'Перевод в нижний регистр: {res()}')