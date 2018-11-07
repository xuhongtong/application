import pymysql

USER='root'
PASSWORD='123456'
HOST='127.0.0.1'
PORT=3306
DB_NAME='test'
CHARSET='utf8'

conn=pymysql.connect(user=USER,password=PASSWORD,host=HOST,port=PORT,db=DB_NAME,charset=CHARSET)


def add():
    with conn.cursor() as cursor:
        # 批量插入数据
        s = [value for value in range(110, 120)]
        sql = "insert into category (cate_id) values(%s)"
        cursor.executemany(sql, s)
        conn.commit()  # 提交数据到数据库
        print(cursor.rowcount)

def modify():
    with conn.cursor() as cursor:
        s = [value for value in range(110, 120)]
        sql='update category set cate_id='


