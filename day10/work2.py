# -*- coding: utf-8 -*-
# @Author  : caijizhi
# @FileName: work2.py
# @Software: PyCharm

class person:
    def __init__(self, age, sex, name):
        self.age = age
        self.sex = sex
        self.name = name


class work(person):

    def startwork(self):
        print(f'{self.name}开始干活')


class student(work):
    def startwork(self):
        print(f'{self.name}正在学习')

    def sing(self):
        print(f'{self.name},今年{self.age}，正在唱歌')


stu = student(20, 30, 50)
stu.startwork()
