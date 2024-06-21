from itertools import combinations

s = [10, 50, 100, 200, 500, 1000, 2000, 5000]
quant = []

for i in range(len(s)):
    for d in combinations(s,2):
        quant.append(sum(d))
    for d in combinations(s,3):
        quant.append(sum(d))
    for d in combinations(s,4):
        quant.append(sum(d))
    for d in combinations(s,5):
        quant.append(sum(d))
    for d in combinations(s,6):
        quant.append(sum(d))
    for d in combinations(s,7):
        quant.append(sum(d))
    for d in combinations(s,8):
        quant.append(sum(d))

quant_rd = []
[quant_rd.append(k) for k in quant if k not in quant_rd]
print(sorted(quant_rd))


