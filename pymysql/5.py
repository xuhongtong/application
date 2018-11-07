import pymysql

USER='root'
PASSWORD='123456'
HOST='127.0.0.1'
PORT=3306
DB_NAME='test'
CHARSET='utf8'

conn=pymysql.connect(user=USER,password=PASSWORD,host=HOST,port=PORT,db=DB_NAME,charset=CHARSET)
with conn.cursor() as cursor:
    values=[value for value in range(20,30)]
    sql="insert into category (cate_id) values(%d)"
    
