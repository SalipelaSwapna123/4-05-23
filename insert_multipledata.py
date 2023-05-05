import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Swapna@2003',database='SKY')
cur=mydb.cursor()
s='insert into cricketer(emp_id,emp_name,salary) values(%s,%s,%s)'
a=[(100,'surya',10000),(101,'sumanth',20000),(103,'sridhar',30000),(105,'rohit',20000)]
cur.executemany(s,a)
mydb.commit()
print("Data inserted successfully")