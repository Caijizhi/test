# -*- coding: utf-8 -*-
# @Author  : caijizhi
# @FileName: Bank.py
# @Software: PyCharm
import random
import pymysql

user={}
def menu():
    """
    界面函数，进行选择业务
    :return:
    """
    print("""
    *********************************
    *       中 国 工 商 银 行         *
    *       账 户 管 理 系 统         *
    *           V1.0                *
    *********************************
    *1.开户                          *
    *2.存钱                          *
    *3.取钱                          *
    *4.转账                          *
    *5.查询                          *
    *6.Bye！                         *
    **********************************
    """)
    choice = input('你要办理什么业务')
    if choice == '1':
        add()
    elif choice == '2':
        account = input('输入你要存钱的账号')
        money = int(input('你要存多少钱'))
        save(account,money)
    elif choice == '3':
        account = input('输入你要取钱的账号')
        pwd = int(input('请输入密码：'))
        money = int(input('你要取多少钱：'))
        take(account,pwd,money)
    elif choice == '4':
        account_out = input('从哪个账号进行划款：')
        pwd = int(input('请输入密码：'))
        account_in = input('向谁转账: ')
        money = int(input('请输入转账金额：'))
        transfer(account_out, pwd,account_in, money)
    elif choice == '5':
        account = input('请输入查询的账号 ')
        pwd = int(input('请输入密码：'))
        search(account,pwd)
    elif choice == '6':
        print('系统关闭')
        exit()
    else:
        print('请输入正确的选项')
def add():
    """
    开户函数
    :return: 1：开户成功，2：账号已存在，3：用户库已满
    """
    global user
    user_info={}
    seed = "1234567890"
    account = []
    for i in range(8):
        account.append(random.choice(seed))
    account1 = ''.join(account)
    print('您当前分配的账号为： ',account1)

    new_name = input('请输入您的姓名')
    new_pwd = int(input('请设置您的密码： '))
    country = input('请输入您的地址')
    province = input('输入省份')
    street = input('输入街道')
    door = input('输入门牌')
    new_money = int(input('你要存多少钱：'))
    bank_addr = '中国工商银行昌平分行'

    for i in user.keys():
        if account == i:
            print('账号已存在')
            return 2
    if len(user)>=100:
        print('用户库已满')
        return 3
    else:
        user_info['账号'] = account1
        user_info['姓名'] = new_name
        user_info['密码'] = new_pwd
        user_info['国家'] = country
        user_info['省份'] = province
        user_info['街道'] = street
        user_info['门牌'] = door
        user_info['存款'] = new_money
        user_info['开户行'] = bank_addr
        user[account1]=user_info
    print(user)

    return 1
def save(account,money):
    """
    :param account: 存钱的账号
    :param money: 存钱金额
    :return: False：代表账号不存在，True：存钱成功
    """
    global user
    if account not in user.keys():
        print('该账户尚未开户，请确认账号')
        return False
    else:
        user[account]['存款']=money+user[account]['存款']
        print('存钱成功，当前账户信息为：',user[account])
        return True
def take(account,pwd,money):
    """
    :param account: 取钱的账号
    :param pwd: 账号密码
    :param money: 取款金额
    :return: 1：代表账号不存在，2：账号密码不匹配，3：余额不够
    """
    global user
    if account not in user.keys():
        print('该账号不存在，请确认账号')
        return 1
    else:
        if pwd==user[account]['密码']:
            if user[account]['存款']>=money:
                user[account]['存款'] = user[account]['存款']-money
                print('取款成功，当前余额为：',user[account]['存款'])
            else:
                print('存款不够，当前存款为',user[account]['存款'])
                return 3
        else:
            print('密码错误')
            return 2
def transfer(out,pwd,ina,money):
    """
    转账函数
    :param out: 转出账号
    :param pwd: 转出账号密码
    :param ina: 转入账号
    :param money: 转钱金额
    :return: 1：转出或者转入的账号错误，2：转出的账号密码不匹配，3：转出账户金额不足
    """
    global user
    if out not in user.keys():
        print('转出账号错误，请确认账号')
        return 1
    if ina not in user.keys():
        print('转入账号错误，请确认账号')
        return 1
    if pwd == user[out]['密码']:
        if user[out]['存款']>=money:
            user[out]['存款']=user[out]['存款']-money
            user[ina]['存款']=user[ina]['存款']+money
            print('转账成功')
        else:
            print('转出账户金额不足')
            return 3
    else:
        print('转出账号密码不匹配')
        return 2
def search(account,pwd):
    """
    :param account: 查询的账号
    :param pwd: 账号的密码
    :return:
    """
    if account not in user.keys():
        print('该用户不存在')
    else:
        if pwd == user[account]['密码']:
            print(f"当前账号：{user[account]['账号']}，密码：{user[account]['密码']}，存款为：{user[account]['存款']}，用户居住地址：{user[account]['国家']},{user[account]['省份']}，{user[account]['街道']}，{user[account]['门牌']}，当前账户的开户行{user[account]['开户行']}")
        else:
            print('账号密码错误')
    return 0
while True:

    menu()
