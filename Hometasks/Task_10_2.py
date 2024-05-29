import openpyexcel
#
from openpyexcel import Workbook, load_workbook, utils
from openpyexcel.worksheet.filters import (Filters, FilterColumn, AutoFilter, CustomFilter, CustomFilters, MinMax)
# wb = Workbook()
# wb.create_sheet("Salary")
# wb.save('salary1.xlsx')

# wb = openpyexcel.load_workbook('salary1.xlsx')
# ws = wb['Salary']
# ws['A1'],ws['A2'], ws['A3']= 'Сидоров','Петров','Иванов'
# ws['B1'],ws['B2'], ws['B3']= '100','200','300'
# print(ws["B1"].value, ws['b2'].value, ws['B3'].value)

wb = openpyexcel.load_workbook('salary1.xlsx')
# wb.create_sheet("Salary_sorted")
# wb.remove_sheet('Sheet') не удалось удалить дефолтный лист®
# ws = wb['Salary']
# wb.active = wb['Salary_sorted']
# ws = wb.active
#filters = ws.auto_filter
# filters.ref = "A1:B3"
# col.filters = Filters(filter=[])
# filters.filterColumn.append(col)

# ws.auto_filter.add_sort_condition(" : ")
wb.save('salary1.xlsx')
