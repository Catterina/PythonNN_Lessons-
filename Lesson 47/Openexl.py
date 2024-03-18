import openpyxl
import random

wb=openpyxl.Workbook()
ws=wb.active
ws.append(['Дебет', 'Кредит','Разница'])


for x in range(10):
    ws.append([random.randint(0,1000), random.randint(0, 1000), f'=SUM(A{x+2}, B{x+2})'])

wb.save('test.xlsx')