import re

s = input()
print(re.findall(r'(\b\d{1,2}\b)', r'0 1 12string 44 20 99 100asd 2'))