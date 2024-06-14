import re


def abbv(x):
    a = re.sub('([а-яА-Я])', '\\1', x).upper()
    b = re.findall(r'\b\w', x)
    return "".join(a), b


print(abbv(input()))