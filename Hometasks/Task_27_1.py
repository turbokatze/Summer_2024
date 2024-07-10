import numpy as np


def ring(rng):
    a = np.arange(1, rng // 2 + 2)[::-1]
    b = np.arange(1, rng // 2 + 1)
    arr_res = np.hstack((b, a))
    return arr_res


def board(i):
    rows = cols = ring(i)
    return np.add.outer(rows, cols)-1

n = int(input())
print(ring(n)) #корректно выводится диапазон кольца доски дартс
print(board(n))
