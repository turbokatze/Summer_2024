import datetime


def freetickets(y, m):
    month3rd = datetime.date(y, m,15)
    dayofweek = month3rd.weekday()
    if dayofweek != 3:
        month3rd = month3rd.replace(day=(15 + (3 - dayofweek) % 7))
    return month3rd


print(f'This year Hermitage free entry Thurdays: ')
for i in range(12):
    print(freetickets(2024,1+i))