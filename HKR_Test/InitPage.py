'''
    1.数据类：
        只准备数据部分：不参与任何操作。
    任务1：
        将这个框架的数据源集中写到excel表里，使用xlrd读取
        xlrd参数化，mysql的参数化。
'''
import xlrd
import pymysql

class ReadMysql:
    conn = pymysql.connect(user='root',password='root',host='localhost',database='hkr')
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql = '''select * from hkrtest'''
    cursor.execute(sql)
    data = cursor.fetchall()
    login_success_data = [data[0],data[1]]
    login_error_data = [data[2],data[3]]
    print(login_success_data)
    print(login_error_data)

class  InitPage:
    wb = xlrd.open_workbook('HKR.xlsx')
    sheet = wb.sheet_by_index(0)
    sheet1 = wb.sheet_by_index(1)
    row = sheet.nrows
    row1 = sheet1.nrows
    login_success_data = []
    login_error_data = []
    #以列表的格式组装测试源，需要进行解包
    for i in range(1,row):
        data = sheet.row_values(i)
        data[1] = str(int(data[1]))
        login_success_data.append(data)
    for j in range(1,row1):
        data = sheet1.row_values(j)
        data[1] = str(int(data[1]))
        login_error_data.append(data)
    #通过列表加字典进行组装数据源在测试用例类不需要解包
    # for i in range(1,row):
    #     data = sheet.row_values(i)
    #     dict1 = {'username':data[0],'password':int(data[1]),'expect':data[2]}
    #     login_success_data.append(dict1)
    # for i in range(1,row1):
    #     data = sheet1.row_values(i)
    #     dict1 = {'username':data[0],'password':int(data[1]),'expect':data[2]}
    #     login_error_data.append(dict1)

    #参考
    # login_error_data = [
    #     # id : msg_uname
    #     {"username": "jason1213123123123", "password": "1234567", "expect": "账户名错误或密码错误!别瞎弄!"},
    #     {"username": "不再爱了", "password": "123456789898945", "expect": "账户名错误或密码错误!别瞎弄!"}
    # ]

















