import openpyexcel


from openpyexcel import Workbook
wb = Workbook()
wb.save('task102.xls')
f_in = open('task102.xls', 'w', encoding='utf-8')
lst = ['\n', '02\n', '03\n']
f_in.writelines(lst)
f_in.close()