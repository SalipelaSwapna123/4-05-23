import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Swapna@2003',database='SKY')
cur=mydb.cursor()
x='update cricketer set salary =salary+123 where emp_id=101'
cur.execute(x)
mydb.commit()