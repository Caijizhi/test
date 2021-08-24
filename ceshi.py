# -*- coding: utf-8 -*-
# @Author  : caijizhi
# @FileName: ceshi.py
# @Software: PyCharm
import xlrd
num = 0
wb = xlrd.open_workbook('12月份衣服销售数据.xlsx')
sheet = wb.sheets()[0]
nrows= sheet.nrows
amout=0
num_yurong = 0
num_niuzaiku = 0
num_fengyi = 0
num_picao = 0
num_t = 0
num_shirt = 0
for i in range (nrows):
    if i == 0:
        print(sheet.row_values(i))
    else:
        price = sheet.row_values(i)[2]
        amout0 = sheet.row_values(i)[4]
        amout = amout0+amout            #计算总销量
        num0 = price*amout0
        num = num+num0                  #计算月销额
        if sheet.row_values(i)[1]=='羽绒服':       #计算羽绒服多少件
            num_yurong1 = sheet.row_values(i)[4]
            num_yurong = num_yurong+num_yurong1
        elif sheet.row_values(i)[1]=='牛仔裤':     #计算牛仔裤多少件
            num_niuzaiku1 = sheet.row_values(i)[4]
            num_niuzaiku = num_niuzaiku+num_niuzaiku1
        elif sheet.row_values(i)[1] == '风衣':    #计算风衣多少件
            num_fengyi1 = sheet.row_values(i)[4]
            num_fengyi = num_fengyi + num_fengyi1
        elif sheet.row_values(i)[1] == '皮草':    #计算皮草多少件
            num_picao1 = sheet.row_values(i)[4]
            num_picao = num_picao + num_picao1
        elif sheet.row_values(i)[1]=='T血':          #计算T血多少件
            num_t1 = sheet.row_values(i)[4]
            num_t = num_t+num_t1
        elif sheet.row_values(i)[1]=='衬衫':          #计算衬衫多少件
            num_shirt1 = sheet.row_values(i)[4]
            num_shirt = num_shirt+num_shirt1
        print(sheet.row_values(i))
print('总销售额为：',num)
print('平均日销量：'+str(int(amout/30))+'件')
print('羽绒服占比：',num_yurong/amout)
print('牛仔裤占比：',num_niuzaiku/amout)
print('风衣占比：',num_fengyi/amout)
print('皮草占比：',num_picao/amout)
print('T血占比：',num_t/amout)
print('衬衫占比：',num_shirt/amout)
