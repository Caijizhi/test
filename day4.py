# -*- coding: utf-8 -*-
# @Author  : caijizhi
# @FileName: day4.py
# @Software: PyCharm
# dict = {"k1":"v1","k2":"v2","k3":"v3"}
# #1、循环遍历出所有的key
# for key in dict.keys():
#     print(key)
# for value in dict.values():
#     print(value)
# dict["k4"] = "v4"
# print(dict)

# info = {
#     '苹果':32.8,
#     '香蕉': 22,
#     '葡萄': 15.5
# }


# Friuts = {
# 	'苹果':12.3,
#     '草莓':4.5,
#     '香蕉':6.3,
#     '葡萄':5.8,
#     '橘子':6.4,
#     '樱桃':15.8
# }
#
# info = {
#     '小明': {
#         'fruits': {'苹果':4, '草莓':13, '香蕉':10},
#         'money': 0
#     },
#     '小刚': {
#         'fruits': {'葡萄':19, '橘子':12, '樱桃':30},
#         'money': 0
#     }
# }
# ming = info['小明'].get('fruits')
# gang = info['小刚'].get('fruits')
# print(ming)
# def count(**kwargs):
#     global Friuts
#     money = 0
#     for key,value in Friuts.items():
#         for name,count in kwargs.items():
#             if key == name:
#                 money = money+(value*count)
#     return money
#
# count(**gang)
# info['小明']['money'] = count(**ming)
# info['小刚']['money'] = count(**gang)
# print(info)

# def count(l=[]):
#     dict = {}
#     for i in l:
#         if i not in dict:
#             dict[i]=1
#         else:
#             dict[i] = dict[i]+1
#     return dict
# print(count([1,2,3,5,6,7,8,2,3,41,2]))

names = [
    ["刘备","56","男","106","IBM", 500 ,"50"],
    ["大乔","19","女","230","微软", 501 ,"60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["张飞", "45", "男", "230", "Tencent", 700 , "10"]
]
data = {}
for i in names:
    info = {'姓名':i[0],'年龄':i[1],'性别':i[2],'编号':i[3],
            '任职公司':i[4],'薪资':i[5],'部门编号':i[6]}
    data[i[0]] = info
print(data)






