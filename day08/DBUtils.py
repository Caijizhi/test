import  pymysql

host="localhost"
user="root"
password="123456"
database="company"

# 增，删，改
def update(sql,param):
    con = pymysql.connect(host=host,user=user,password=password,database=database)
    cursor = con.cursor()
    cursor.execute(sql,param)
    con.commit()
    cursor.close()
    con.close()

def select(sql,parm,mode="all",size=1):
    con = pymysql.connect(host=host,user=user,password=password,database=database)
    cursor = con.cursor()
    cursor.execute(sql,parm)
    con.commit()

    #提取数据
    data = ""
    if mode == "all":
        data = cursor.fetchall()
    elif mode == "one":
        data = cursor.fetchone()
    elif mode == "many":
        data = cursor.fetchmany(size)

    cursor.close()
    con.close()
    return data

sql = 'select * from t_dept'
f = select(sql = sql,parm=None,mode='all')






















