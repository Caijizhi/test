# -*- coding: utf-8 -*-
# @Author  : caijizhi
# @FileName: Bankdata.py
# @Software: PyCharm
import random
import pymysql
user={}
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

    try:
        con = pymysql.connect(user='root', passwd='123456',
                              host='localhost', db='bank', port=3306, charset='utf8')
    except Exception:
        print('连接失败，请检查连接')
    else:
        cur = con.cursor(pymysql.cursors.DictCursor)
    sql = 'select * from userinfo'
    cur.execute(sql)
    user = cur.fetchall()
    cur.close()
    con.close()

    newuser ={}
    for i in user:
        num = i['account']
        newuser[num]=i
    return newuser
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
        money = float(input('你要存多少钱'))
        save(account,money)
    elif choice == '3':
        account = input('输入你要取钱的账号')
        pwd = int(input('请输入密码：'))
        money = float(input('你要取多少钱：'))
        take(account,pwd,money)
    elif choice == '4':
        account_out = input('从哪个账号进行划款：')
        pwd = int(input('请输入密码：'))
        account_in = input('向谁转账: ')
        money = float(input('请输入转账金额：'))
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
    user=getall()
    seed = "1234567890"
    account = []
    for i in range(8):
        account.append(random.choice(seed))
    account1 = ''.join(account)
    print('您当前分配的账号为： ',account1)
    try:
        new_name = input('请输入您的姓名')
        new_pwd = int(input('请设置您的六位数字密码： '))
        country = input('请输入您的国家')
        province = input('输入省份')
        street = input('输入街道')
        door = input('输入门牌')
        new_money = float(input('你要存多少钱：'))
    except Exception:
        print('您输入的信息不合法，请重新选择业务')
        menu()
    bank_addr = '中国工商银行昌平分行'

    for i in user.keys():
        if account == i:
            print('账号已存在')
            return 2
    if len(user)>=100:
        print('用户库已满')
        return 3
    else:
        try:
            sql = "insert into userinfo(account,username,password,country,province,street,door,money,bankname) values('%s','%s','%d','%s','%s','%s','%s','%f','%s')" % \
                  (account1,new_name,new_pwd,country,province,street,door,new_money,bank_addr)
            update(sql)
        except Exception:
            print('出现了未知错误，重新开户')
        else:
            print(f"""     
                    开户成功
                账号：{account1}
                用户名：{new_name}
                密码：{new_pwd}
                地址：{country}{province}{street}{door}
                存款：{new_money}
                开户行：{bank_addr}
""")
    return 1
def save(account,money):
    """
    :param account: 存钱的账号
    :param money: 存钱金额
    :return: False：代表账号不存在，True：存钱成功
    """
    user = getall()
    if account not in user.keys():
        print('该账号尚未开户，请确认账号')
        return False
    else:
        new_money = user[account]['money']+money
        sql = "update userinfo set money = '%s' where account = '%s'" % (new_money, account)
        update(sql)
        print(f'存钱成功，当前余额为{new_money}')
        return True
def take(account,pwd,money):
    """
    :param account: 取钱的账号
    :param pwd: 账号密码
    :param money: 取款金额
    :return: 1：代表账号不存在，2：账号密码不匹配，3：余额不够
    """
    user = getall()
    if account not in user.keys():
        print('该账号不存在，请确认账号')
        return 1
    else:
        if pwd==user[account]['password']:
            if user[account]['money']>=money:
                new_money = user[account]['money']-money
                sql = "update userinfo set money = '%s' where account = '%s'" % (new_money, account)
                update(sql)
                print('取款成功，当前余额为：',new_money)
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
    user = getall()
    if out not in user.keys():
        print('转出账号错误，请确认账号')
        return 1
    if ina not in user.keys():
        print('转入账号错误，请确认账号')
        return 1
    if pwd == user[out]['password']:
        if user[out]['money']>=money:
            out_money=user[out]['money']-money
            in_money=user[ina]['money']+money
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
def search(account,pwd):
    """
    :param account: 查询的账号
    :param pwd: 账号的密码
    :return:
    """
    user = getall()
    if account not in user.keys():
        print('该用户不存在')
    else:
        if pwd == user[account]['password']:
            print(f"当前账号：{user[account]['account']}，密码：{user[account]['password']}，存款为：{user[account]['money']}，用户居住地址：{user[account]['country']},{user[account]['province']}，{user[account]['street']}，{user[account]['door']}，当前账户的开户行{user[account]['bankname']}")
        else:
            print('账号密码错误')
    return 0
while True:
    menu()



