def indexlist():
    lst1 = list(input())
    indexmin = min(lst1)
    indexmax = max(lst1)
    indmin = [i for i, k in enumerate(lst1) if k == indexmin]
    indmax = [i for i, k in enumerate(lst1) if k == indexmax]
    return indmin, indmax


print('Enter numbers list: ')
indmin, indmax = indexlist()
print(f'Min numbers index: {indmin}, Max numbers index: {indmax}')