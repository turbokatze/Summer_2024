salary_list = []
i = 0
while True:
    salary = int(input())
    salary_list.append(i)
    i = salary
    if salary == 0:
        break
print(sum(salary_list) / float(len(salary_list[:-1])))
