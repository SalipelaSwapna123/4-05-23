import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Swapna@2003',database='SKY')
cur=mydb.cursor()
f='select * from cricketer where emp_id=100'
cur.execute(f)
display=cur.fetchall()
for x in display:
    print(x)