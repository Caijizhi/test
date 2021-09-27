# -*- coding: utf-8 -*-
# @Author  : caijizhi
# @FileName: readcase.py
# @Software: PyCharm
import xlrd
def readxlsx():

    case = [[],[],[],[],[]]
    wb = xlrd.open_workbook(filename='测试用例.xlsx')
    for i in range(5):
        sheet = wb.sheet_by_index(i)
        rows = sheet.nrows
        for j in range(rows):
            data = sheet.row_values(j)
            case[i].append(data)
    return case