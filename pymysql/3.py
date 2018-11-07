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
    with conn.cursor() as cursor:
        values=[str(item) for item in range(11,21)]
        sql="insert into category(cate_id) values (%s);"
        cursor.executemany(sql,values)
        conn.commit()
        if cursor.rowcount:
            print('添加成功')
        else:
            print('添加失败')

insert_many()