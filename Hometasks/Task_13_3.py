def genalter():
    i = 1
    while True:
        for _ in range(i):
            if i % 2 == 1:
                yield i
            else:
                yield -i
            i += 1
        # if i > 10: #for test, res: 1 -2 3 -4 5 -6 7 -8 9 -10 11 -12 13 -14 15
        #     break

fg1 = genalter()
while True:
    print(next(fg1), end=' ')
