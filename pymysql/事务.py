import pymysql
import logging

USER = 'root'
PASSWORD = '123456'
HOST = '127.0.0.1'
PORT = 3306
DB_NAME = 'test'
CHARSET = 'utf8'

conn = pymysql.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, db=DB_NAME, charset=CHARSET)
# conn.begin()
with conn.cursor() as cursor:
    try:
        conn.begin()
        sql1 = "select name,money from user where name='小王';"
        cursor.execute(sql1)
        result = cursor.fetchone()
        money = result[1] - 200
        sql2 = "update user set money=%s where name='小王'" % money
        # sql2 = "update user set money=800 where name='小王'"
        cursor.execute(sql2)
        sql3 = "select name,money from user where name='小李';"
        cursor.execute(sql3)
        result = cursor.fetchone()
        money = result[1] + 200
        sql4 = "update user set money=%s where name='小李';" % money
        cursor.execute(sql4)
        conn.commit()
    except Exception as e:
        logging.debug(e)
        conn.rollback()
