def camel(n):
     n = ' '.join(word.capitalize() for word in n.split())
     return n.replace(' ','')

print(camel(input('Введите слова через пробел: ')))