# -*- coding: utf-8 -*-
# @Author  : caijizhi
# @FileName: 需求编程.py
# @Software: PyCharm
'''
i.	定义了一个学生类：
属性:学号，姓名，年龄，性别，身高，体重，成绩，家庭地址，电话号码。
行为：学习（要求参数传入学习的时间），
    玩游戏（要求参数传入游戏名），
    编程（要求参数传入写代码的行数），
    数的求和（要求参数用变长参数来做，返回求和结果）
'''
class Student:
    def __init__(self,no,name,age,sex,height,weight,score,addr,phone):
        self.__no = no
        self.__name = name
        self.__age = age
        self.__sex = sex
        self.__height = height
        self.__weight = weight
        self.__score = score
        self.__addr = addr
        self.__phone = phone
    def learn(self,time):
        print(f'{self.__name}已经学习了{time}小时')
    def play(self,game):
        print(f'{self.__name}正在完{game}')
    def code(self,line):
        print(f'{self.__name}正在编程，已经写了{line}行了')
    def addnum(self,*a,**b):
        return a+b




class Car:
    def __init__(self,brand,wheel,color,weight,oil):
        self.__brand = brand
        self.__wheel = wheel
        self.__color = color
        self.__weight = weight
        self.__oil = oil

    def run(self,func):
        print(f'{self.__brand}的车能够{func}')

Ferrari = Car('法拉利',4,'红色','500kg','50L')
Ferrari.run('赛车')
bmw = Car('宝马',4,'白色','450kg','45L')
bmw.run('通勤')
linmu = Car('铃木',2,'黑色','250kg','15L')
linmu.run('越野')
wulin = Car('五菱',4,'白色','350kg','35L')
wulin.run('越野')
tlj = Car('拖拉机',6,'白色','550kg','55L')
tlj.run('拉货')


class Comp:

    def __init__(self,brand,color,weight,disk,cpu,memory,useTime):
        self.__brand = brand
        self.__useTime = useTime
        self.__color = color
        self.__weight = weight
        self.__cpu = cpu
        self.__memory = memory
        self.__disk = disk
    def play(self,game):
        print(f'{self.__cpu}，{self.__memory}内存的电脑打{game}一点不卡')
    def work(self):
        print(f'{self.__cpu}，{self.__memory}内存的电脑进行办公')


class Monkey:
    def __init__(self,sort,sex,color,weight):
        self.__sort = sort
        self.__sex = sex
        self.__color = color
        self.__weight = weight

    def fire(self,material):
        print(f'{self.__sort}正在用{material}造火')

    def learn(self,*thing):
        for i in thing:
            print(f'{self.__sort}正在学习{i}')
monkey1 = Monkey('长臂猿','men','黄色','50kg')
monkey1.learn('电脑','吃饭','睡觉')
