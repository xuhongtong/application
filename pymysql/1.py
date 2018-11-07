import pymysql

conn=pymysql.connect(user='root',passwd='123456',host='127.0.0.1',port=3306,db='test',charset='utf8')

cursor=conn.cursor()
sql='select * from emp'
cursor.execute(sql)
results=cursor.fetchone()
print(results)
# for result in results:
#     print(result[0])
#     print(result[1])

cursor.close()
conn.close()