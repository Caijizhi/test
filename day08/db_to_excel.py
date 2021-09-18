# -*- coding: utf-8 -*-
# @Author  : caijizhi
# @FileName: db_to_excel.py
# @Software: PyCharm

import pymysql
import xlwt

def db_to_excel(host,user,pwd,dbname,tablename,outpath):
    conn = pymysql.connect(host=host,user=user,password=pwd,database=dbname)
    cursor = conn.cursor()
    sql = 'select * from '+tablename
    cursor.execute(sql)
    result = cursor.fetchall()
    desc = cursor.description
    conn.commit()
    cursor.close()
    conn.close()
    workbook = xlwt.Workbook()
    print(result)
    sheet = workbook.add_sheet(tablename)
    for colum in range(0,len(desc)):
        print(desc[colum][0])
        sheet.write(0,colum,desc[colum][0])
    row = 1
    col = 0
    for row in range(1,len(result)+1):
        for col in range(0,len(result[0])):
            sheet.write(row,col,result[row-1][col])
    workbook.save(outpath)

db_to_excel('localhost','root','123456','company','t_dept','dept.xls')
db_to_excel('localhost','root','123456','company','t_employees','emp.xls')

