# -*- coding: utf-8 -*-
# @Author  : caijizhi
# @FileName: TestBank.py
# @Software: PyCharm、
from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
import NewBank
from NewBank import Bank
import xlrd
import readcase
cases = readcase.readxlsx()

adduser = cases[0]
savedata = cases[1]
getdata = cases[2]
trandata = cases[3]
serchdata = cases[4]


@ddt
class TestBank(TestCase):

    @data(*adduser)
    @unpack
    def testAdd(self,a,b,c,d,e,f,g,flag):
        bank = Bank(alluser=NewBank.getall())
        sum0 = bank.creatAccount(a,b,c,d,e,f,g)
        self.assertEqual(sum0,flag)


    @data(*savedata)
    @unpack
    def testSave(self,a,b):
        bank = Bank(alluser=NewBank.getall())
        sum = bank.saveMoney(a,b)
        self.assertTrue(sum)
    @data(*getdata)
    @unpack
    def testget(self,a,b,c,d):
        bank = Bank(alluser=NewBank.getall())
        result = bank.getMoney(a,b,c)
        self.assertEqual(result,d)

    @data(*trandata)
    @unpack
    def testtran(self,a,b,c,d,flag):
        bank = Bank(alluser=NewBank.getall())
        result = bank.tranMoney(a,b,c,d)
        self.assertEqual(result,flag)

    @data(*serchdata)
    @unpack
    def testserch(self,a,b,flag):
        bank = Bank(alluser=NewBank.getall())
        result = bank.serch(a,b)
        self.assertEqual(result, flag)

