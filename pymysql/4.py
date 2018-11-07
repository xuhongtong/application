import pymysql


USER='root'
PASSWORD='123456'
HOST='127.0.0.1'
PORT=3306
DB_NAME='test'
CHARSET='utf8'
def insert_many():

    conn=pymysql.connect(user=USER,
                         password=PASSWORD,
                         host=HOST,
                         port=PORT,
                         db=DB_NAME,
                         charset=CHARSET)
    conn.begin()
    with conn.sursor() as cursor:
        sql1='select uid,username,price from user where uid=1'
        cursor.execute(sql1)
        result=cursor.fetchone()
        price=result[2]-500
        sql2='update user set price=%s where uid=1 %(price)'

        sql3 = 'select uid,username,price from user where uid=2'
        cursor.execute(sql3)
        result = cursor.fetchone()
        price = result[2] + 500
        sql4 = 'update user set price=%s where uid=2 %(price)'

    conn.rollback()

