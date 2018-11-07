import pymysql

#建立连接
conn=pymysql.connect(user='root',password='123456',host='127.0.0.1',port=3306,db='test')

#创建游标对象
sursor=conn.cursor()

#执行sql语句
sql='select * from emp;'
sursor.execute(sql)

#处理数据
results=sursor.fetchall()
for result in results:
    print(result[0])

#关闭连接
sursor.close()
conn.close()