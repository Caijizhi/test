# -*- coding: utf-8 -*-
# @Author  : caijizhi
# @FileName: excel_to_db.py
# @Software: PyCharm
import pymysql
import xlrd
from DBUtils import update
wb = xlrd.open_workbook(filename=r'2020年每个月的销售情况.xlsx')
sql = "insert into sold values (%s,%s,%s,%s,%s)"
parm = []
for i in range(12):
    sheet = wb.sheet_by_index(i)
    rows = sheet.nrows
    for j in range(1,rows):
        data = sheet.row_values(j)
        parm = [f'{i+1}月{data[0]}',data[1],data[2],data[3],data[4]]
        update(sql,parm)