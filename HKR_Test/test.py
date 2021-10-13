# -*- coding: utf-8 -*-
# @Author  : caijizhi
# @FileName: test.py
# @Software: PyCharm
import xlrd



wb = xlrd.open_workbook('HKR.xlsx')
sheet = wb.sheet_by_index(0)
row = sheet.nrows
for i in range(1, row):
    data = sheet.row_values(i)
    print(data[1])
