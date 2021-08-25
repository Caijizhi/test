# -*- coding: utf-8 -*-
# @Author  : caijizhi
# @FileName: guessnum.py
# @Software: PyCharm
import random
money = 2000
num = 0
choice = 0
def createnum():
    global num,choice
    num = random.randint(1,100)

def judge():
    global money,num,choice

    while money>0:
        choice = int(input('请猜数字吧'))
        if choice==num:
            print("恭喜,猜对了")
            money+=5000

            time = input('是否继续 Y/N')
            if time == 'Y':
                createnum()
                judge()
            elif time == 'N':
                print('剩余金币为'+str(money)+'再见')
                exit()
            else:
                exit()
        else:
            if choice>num:
                print("大了")
                money = money-200
                print('当前金币为',money)
            else:
                print("小了")
                money = money-200
                print('当前金币为', money)
    if money == 0:
        print('没钱玩个屁')
createnum()
judge()