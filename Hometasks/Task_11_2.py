# import openpyexcel
# from openpyexcel import Workbook, load_workbook, utils
# from openpyexcel.worksheet.filters import (Filters, FilterColumn, AutoFilter, CustomFilter, CustomFilters, MinMax)
#
# f = open("salarylist.txt", "wt", encoding='utf-8')
# f.write('1, Иван, Иванов, Вектор, 200\n' '2, Борис, Борисов, Гамма, 400\n' '3, Евгения, Евгеньева, Омега, 300')
# f.close()
#
# wb = Workbook()
# wb.create_sheet("Salarylist")
# wb.save('sortedlist.xlsx')
#
# excel_data = []
#
# with open("salarylist.txt", "r") as handle:
#     content = handle.readlines()
#
# for line in content:
#     if not ("Firstname") in line:
#                 line = line.replace(","," ")
#                 excel_data.append(line)
#
# with open("sortedlist.xlsx", "w") as excel_handle:
#     for line in excel_data:
#         excel_handle.write(line)
#
# wb.save('sortedlist.xlsx')


