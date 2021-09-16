# -*- coding: utf-8 -*-
# @Author  : caijizhi
# @FileName: NewBank.py
# @Software: PyCharm
'''
银行类： 存储用户的表
        进行业务操作
            开户
            存钱
            取钱
            转账
            查询

账户类：账号，姓名，密码，（地址类：国家，省份，街道，门牌）
'''
import random
import time
import pymysql

bank_addr = '中国工商银行昌平分行'


class Address:
    def __init__(self, country, province, street, door):
        self.country = country
        self.province = province
        self.street = street
        self.door = door


class User(Address):
    def __init__(self, id, name, pwd, money, addr):
        self.id = id
        self.name = name
        self.pwd = pwd
        self.money = money
        self.addr = addr

    def __str__(self):
        return f'''
    当前账户信息为：   账号：{self.id}，
                    姓名：{self.name}，
                    密码：{self.pwd}
                    金额：{self.money}
                    地址:{self.addr.country}
                        {self.addr.province}
                        {self.addr.street}
                        {self.addr.door}
'''


class Bank():
    def __init__(self, alluser):
        self.alluser = alluser

    def creatAccount(self):
        '''
        开户函数
        :return:
        '''
        seed = "1234567890"
        account = []
        for i in range(8):
            account.append(random.choice(seed))
        account1 = ''.join(account)
        print('您当前分配的账号为： ', account1)
        try:
            new_name = input('请输入您的姓名')
            new_pwd = int(input('请设置您的六位数字密码： '))
            country = input('请输入您的国家')
            province = input('输入省份')
            street = input('输入街道')
            door = input('输入门牌')
            addr = Address(country, province, street, door)
            new_money = float(input('你要存多少钱：'))
        except Exception:
            print('您输入的信息不合法')
            main()

        user = User(account1, new_name, new_pwd, new_money, addr)
        if account1 in self.alluser.keys():
            print('当前账号已存在，重新开户')
            return 2
        if len(self.alluser) >= 100:
            print('用户库已满，请去别的银行开户')
        else:
            try:
                sql = "insert into userinfo(account,username,password,country,province,street,door,money,bankname) values('%s','%s','%d','%s','%s','%s','%s','%f','%s')" % \
                      (account1, new_name, new_pwd, country, province, street, door, new_money, bank_addr)
                update(sql)
            except Exception:
                print('出现了未知错误，重新开户')
            else:
                print(user)

    def saveMoney(self, account, money):
        '''
        :param account: 存钱的账户
        :param money: 存入的金额
        :return:
        '''
        if account not in self.alluser.keys():
            print('该账号尚未开户，请确认账号')
            return False
        else:
            newmoney = self.alluser[account]['money'] + money
            sql = "update userinfo set money = '%s' where account = '%s'" % (newmoney, account)
            update(sql)
            print(f'存钱成功，当前余额为{newmoney}')
            return True

    def getMoney(self, account, pwd, money):
        '''

        :param account: 取钱的账号
        :param pwd: 取钱的密码
        :param money: 取钱的金额
        :return:
        '''
        if account not in self.alluser.keys():
            print('该账号不存在，请确认账号')
            return 1
        else:
            if pwd == self.alluser[account]['password']:
                if self.alluser[account]['money'] >= money:
                    new_money = self.alluser[account]['money'] - money
                    sql = "update userinfo set money = '%s' where account = '%s'" % (new_money, account)
                    update(sql)
                    print('取款成功，当前余额为：', new_money)
                else:
                    print('存款不够，当前存款为', self.alluser[account]['存款'])
                    return 3
            else:
                print('密码错误')
                return 2

    def tranMoney(self, out, pwd, ina, money):
        '''
        转账函数
        :param out:转出的账户
        :param pwd: 转出账户的密码
        :param ina: 转入的账户
        :param money: 转出的金额
        :return:
        '''
        if out not in self.alluser.keys():
            print('转出账号错误，请确认账号')
            return 1
        if ina not in self.alluser.keys():
            print('转入账号错误，请确认账号')
            return 1
        if pwd == self.alluser[out]['password']:
            if self.alluser[out]['money'] >= money:
                out_money = self.alluser[out]['money'] - money
                in_money = self.alluser[ina]['money'] + money
                sql1 = "update userinfo set money = '%s' where account = '%s'" % (out_money, out)
                sql2 = "update userinfo set money = '%s' where account = '%s'" % (in_money, ina)
                update(sql1)
                update(sql2)
                print('转账成功')
            else:
                print('转出账户金额不足')
                return 3
        else:
            print('转出账号密码不匹配')
            return 2

    def serch(self, account, pwd):
        if account not in self.alluser.keys():
            print('该用户不存在')
        else:
            if pwd == self.alluser[account]['password']:
                print(f'''
                ----------------账号信息------------------
                账号：{self.alluser[account]['account']}
                密码：******
                存款：{self.alluser[account]['money']}、
                用户居住地：{self.alluser[account]['country']}{self.alluser[account]['province']}{self.alluser[account]['street']}{self.alluser[account]['door']}
                当前开户行：{self.alluser[account]['bankname']}
                ''')
            else:
                print('账号密码错误')


def update(sql):
    try:
        con = pymysql.connect(user='root', passwd='123456',
                              host='localhost', db='bank', port=3306, charset='utf8')
    except Exception:
        print('连接失败，请检查连接')
    else:
        cur = con.cursor(pymysql.cursors.DictCursor)
        cur.execute(sql)
        con.commit()
        cur.close()


def getall():
    '''
    获取数据库所有数据，并转化为字典
    :return: newuser字典类型的数据
    '''
    try:
        con = pymysql.connect(user='root', passwd='123456',
                              host='localhost', db='bank', port=3306, charset='utf8')
    except Exception:
        print('连接失败，请检查连接')
    else:
        cur = con.cursor(pymysql.cursors.DictCursor)
    sql = 'select * from userinfo'
    cur.execute(sql)
    user = cur.fetchall()  # user是个列表
    cur.close()
    con.close()
    newuser = {}
    for i in user:  # 转化为字典
        num = i['account']
        newuser[num] = i
    return newuser


def main():
    while True:
        alluser = getall()
        atm = Bank(alluser)
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
            atm.creatAccount()
        elif choice == '2':
            account = input('输入你要存钱的账号')
            money = float(input('你要存多少钱'))

            atm.saveMoney(account, money)
        elif choice == '3':
            account = input('输入你要取钱的账号')
            pwd = int(input('请输入密码：'))
            money = float(input('你要取多少钱：'))

            atm.getMoney(account, pwd, money)
        elif choice == '4':
            account_out = input('从哪个账号进行划款：')
            pwd = int(input('请输入密码：'))
            account_in = input('向谁转账: ')
            money = float(input('请输入转账金额：'))

            atm.tranMoney(account_out, pwd, account_in, money)
        elif choice == '5':
            account = input('请输入查询的账号 ')
            pwd = int(input('请输入密码：'))

            atm.serch(account, pwd)
        elif choice == '6':
            print('系统关闭')
            exit()
        else:
            print('请输入正确的选项')


if __name__ == '__main__':
    main()
