# -*- coding: utf-8 -*-
# @Author  : caijizhi
# @FileName: work3.py
# @Software: PyCharm

class Oldphone:
    __brand = ''

    def setBrand(self, brand):
        self.__brand = brand

    def getBrand(self):
        return self.__brand

    def call(self, name):
        print(f'正在给{name}打电话')


class Newphone(Oldphone):
    def call(self, name):
        print('语音拨号中.....')
        super().call(name)

    def show(self):
        print(f'品牌为：{self.getBrand()}的手机很好用...')


class Test:
    p = Newphone()
    p.setBrand('华为')
    p.show()
    p.call('张三')


Test
