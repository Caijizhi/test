'''
    xlrd:读取
    xlwt:写入
    xlrd:0.9.3版本
    xlwt:

    python -m  pip install   xlrd==0.9.3

    1.步骤
    1.打开工作簿
    2.找到你想操作的选项卡
    3.通过坐标读取数据
任务1：
    把2020年的所有数据统计分析并打印出来
    全年的销售总额    2400069.0
    每件衣服的销售（件数）占比  ok
    每件衣服的月销售占比  ok
    每件衣服的销售额占比  ok

    最畅销的衣服是那种   ok
    每个季度最畅销的衣服
    全年销量最低的衣服   ok

任务2：
    把excel表的所有数据存储到数据库。
任务3：
    将三国集团数据，导出到excel里。
'''
import xlrd

#1.打开
wb = xlrd.open_workbook(filename=r'2020年每个月的销售情况.xlsx')
# 2.操作选项卡

sheet = wb.sheet_by_name("1月")

sum = 0
amount = 0
count = {}
m_count = {}

rows = sheet.nrows # 获取有多少行


def getinfo(mon):
    p_info = {}
    p_account = 0
    sheet = wb.sheet_by_index(mon-1)
    rows = sheet.nrows
    for j in range(1,rows):
        data =sheet.row_values(j)
        p_account = p_account +data[4]
        if data[1] not in p_info.keys():
            p_info[data[1]] = data[4]
        else:
            p_info[data[1]] = p_info[data[1]]+data[4]
    for i in p_info.keys():
        j = format(round(p_info[i] / p_account, 4), '.2%')
        print(f'{mon}月{i}的销量占比{j}')
    return p_info,p_account

def getmax(s):
    max = 0
    for key, value in s.items():
        if value > max:
            max = value

    for key, value in s.items():
        if value == max:
            print('最畅销的衣服是', key, '销量是', max, '件')
            break;
    print('dsada')

def getmaxseason():
    first = {}
    amount1 = 0
    second = {}
    third = {}
    four = {}

    for i in range(2,5):
        sheet = wb.sheet_by_index(i)
        rows = sheet.nrows
        for j in range(1, rows):
            data = sheet.row_values(j)
            amount1 = amount1+data[4]
            if data[1] not in first.keys():
                first[data[1]] = int(data[4])
            else:
                first[data[1]] = int(first[data[1]]+data[4])
    for i in range(5,8):
        sheet = wb.sheet_by_index(i)
        rows = sheet.nrows
        for j in range(1, rows):
            data = sheet.row_values(j)
            amount1 = amount1 + data[4]
            if data[1] not in second.keys():
                second[data[1]] = int(data[4])
            else:
                second[data[1]] = int(second[data[1]] + data[4])
    for i in range(8,11):
        sheet = wb.sheet_by_index(i)
        rows = sheet.nrows
        for j in range(1, rows):
            data = sheet.row_values(j)
            amount1 = amount1+data[4]
            if data[1] not in third.keys():
                third[data[1]] = int(data[4])
            else:
                third[data[1]] = int(third[data[1]]+data[4])
    for i in range(11,14):#11,12,13
        sheet = wb.sheet_by_index(i%12)
        rows = sheet.nrows
        for j in range(1, rows):
            data = sheet.row_values(j)
            amount1 = amount1+data[4]
            if data[1] not in four.keys():
                four[data[1]] = int(data[4])
            else:
                four[data[1]] = int(four[data[1]]+data[4])
    getmax(first)
    getmax(second)
    getmax(third)
    getmax(four)



for i in range(12):
    sheet = wb.sheet_by_index(i)
    rows = sheet.nrows
    for j in range(1,rows):
        data = sheet.row_values(j)
        sum = sum + data[2]*data[4]
print("全年销售总额：￥",round(sum,2))


for i in range(12):     #全年销售情况
    sheet = wb.sheet_by_index(i)
    rows = sheet.nrows
    for j in range(1,rows):
        data = sheet.row_values(j)
        amount = amount + data[4]
        num = float(data[2] * data[4])
        if data[1] not in count.keys():
            count[data[1]] = {'数量':data[4],'销售额':num}
        else:
            count[data[1]]['数量']= count[data[1]]['数量']+data[4]
            count[data[1]]['销售额'] = round((count[data[1]]['销售额'] + num),2)

for i in count.keys():
    j = format(round(count[i]['数量']/amount,4),'.2%')
    print(i,'销量占比',j)

for i in count.keys():
    j = format(round(count[i]['销售额']/sum,4),'.2%')
    print(i,'销售额占比',j)

max = 0
min = 9999

for key,value in count.items():
    if value['数量']>max:
        max = value['数量']

for key,value in count.items():
    if value['数量']==max:
        print('最畅销的衣服是',key,'销量是',max,'件')
        break;


for key,value in count.items():
    if value['数量']<min:
        min = value['数量']

for key,value in count.items():
    if value['数量']==min:
        print('最不畅销的衣服是',key,'销量是',min,'件')
        break;


print(amount)
print(count)
getmaxseason()
