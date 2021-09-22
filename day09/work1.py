# -*- coding: utf-8 -*-
# @Author  : caijizhi
# @FileName: work1.py
# @Software: PyCharm
class Bottle:

    def __init__(self,height,volume,color,material):
        self.__height = height
        self.__volume = volume
        self.__color = color
        self.__material = material
    def __str__(self):
        return f"{self.__height}高{self.__volume}毫升{self.__material}材质{self.__color}的水杯"
    def saveWate(self):
        print(f"{self.__height}高{self.__material}材质{self.__color}的水杯能够装{self.__volume}毫升的液体")


b1 = Bottle(height='20cm',volume=3000,color='蓝色',material='玻璃')

print(b1)
b1.saveWate()

class Comp:

    def __init__(self,screenSize,price,cpu,memory,useTime):
        self.__screenSize = screenSize
        self.__price = price
        self.__cpu = cpu
        self.__memory = memory
        self.__useTime = useTime
    def type(self):
        print(f'我正在用价格为{self.__price}，CPU型号是{self.__cpu}的电脑打字')
    def palyGame(self):
        print(f'{self.__cpu}，{self.__memory}内存的电脑打游戏一点不卡')
    def watchMovie(self):
        print(f'{self.__screenSize}的屏幕可以看{self.__useTime}的电影')

DELL = Comp('10寸',5999,'i7','1TB','5小时')
DELL.type()
DELL.palyGame()
DELL.watchMovie()