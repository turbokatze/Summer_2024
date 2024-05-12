numbers = str(input())
res = []

for i, k in enumerate(numbers):
    res.append(k*(i+1))

res.count([])
print(res)
