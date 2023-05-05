import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Swapna@2003',database='SKY')
cur=mydb.cursor()
s='insert into cricketer(emp_id,emp_name,salary) values(%s,%s,%s)'
a=(100,'shubman Gill',10000)
cur.execute(s,a)
mydb.commit()
print("Data inserted successfully")