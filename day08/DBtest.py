from  DBUtils import update
from DBUtils import select

# sql = "update t_employees  set sal = sal + %s"
# param = [100]
#


sql1 = "select * from t_employees  where sal > %s and comm > %s"
param1 = [2000,100]

data = select(sql1,param1,mode="many",size=4)
for i in data:
    print(i)





