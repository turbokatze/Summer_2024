def dct_rec(n):
    dctn = {}
    for k, v in n.items():
        # if v in dctn:
        #     dctn.update(dct_rec(v))
        # else:
        #     dctn[k] = v
    return dctn

dct1 = {1:1, 2:2, 3:{2:22, 3:{1:111, 2:222, 3:{0:1111, 1:2222, 2:3333}}, 1:11,}, 6:22}
dct2 = dct_rec(dct1)

user_input = input()
if user_input in dct1:
    print(dct1.keys())
else:
    print('error')