# -*- coding: utf-8 -*-
# @Author  : caijizhi
# @FileName: work1.py
# @Software: PyCharm

class chef:
    __name = ''
    __age = ''
    # def __init__(self,name,age):
    #     self.__name = name
    #     self.__age = age

    def setName(self,name):
        self.__name = name
    def setAge(self,age):
        self.__age = age
    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
    def firerice(self):
        pass

class chefson(chef):
    def cook(self):
        pass
class chefgrandson(chefson):
    def firerice(self):
        super().firerice()
        print('蒸饭')
    def cook(self):
        print('炒菜')

class test:
    stu = chefgrandson()
    stu.setAge(20)
    stu.setName('zhangsan')
    print(stu.getName(),stu.getAge())

test