n = int(input())
fnumber = 1
if n >= 1:
    for i in range(1, n + 1):
        fnumber = fnumber * i

print(f'факториал {n}: {fnumber}')