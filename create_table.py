import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Swapna@2003',database='SKY')
cur=mydb.cursor()
t='create table cricketer(emp_id integer(4),emp_name varchar(20),salary integer(10))'
# alter and update can be done here and after that we can commit fun will be use
cur.execute(t)