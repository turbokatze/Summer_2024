# f = open("test1.txt", "wt", encoding='utf-8')
# f.write('Мой дядя самых честных правил\n' 'Когда не в шутку занемог\n')
# f.close()

with open('test1.txt', 'r') as sourcetxt, open('test2.txt', 'w') as reversetxt:
    for line in reversed(sourcetxt.readlines()):
        for word in reversed(line.split()):
            reversetxt.write(word); reversetxt.write(' ')
        reversetxt.write('\n')
