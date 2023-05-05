import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Swapna@2003',database='SKY')
cur=mydb.cursor()
s='delete from cricketer where emp_id=100'
cur.execute(s)
mydb.commit()