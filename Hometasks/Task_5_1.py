user_input = int(input())
lst1 = []
for i in range(user_input):
  lst1.append([])
  lst1[i].append(1)
  for c in range(1, i):
    lst1[i].append(lst1[i - 1][c - 1] + lst1[i - 1][c])
  if(user_input > 0):
    lst1[i].append(1)
for i in range(user_input):
  print('' * (user_input - i))
  for c in range(0, i + 1):
    print('{0:1}'.format(lst1[i][c]), end =' ')
print()