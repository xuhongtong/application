import pymysql
from settings import db

'''
封装内容：
配置数据库连接信息
创建数据库连接
创建游标对象
执行sql语句
关闭游标及连接
'''


class InitMsql:
    def __init__(self):
        self.conn = self.conn_mysql
        self.cursor = self.get_cursor

    # 创建数据库连接
    @property
    def conn_mysql(self):
        return pymysql.connect(user=db['USER'], password=db['PASSWORD'], db=db['DB'], host=db['HOST'], port=db['PORT'])

    # 创建游标对象
    @property
    def get_cursor(self):
        return self.conn.cursor()

    # 执行sql语句
    def exec_sql(self, *args):
        self.cursor.execute(*args)
        self.conn.commit()
        self.close()

    # 关闭连接
    def close(self):
        self.cursor.close()
        self.conn.close()


# 调用封装
if __name__ == '__main__':
    helper = InitMsql()
    sql = 'insert into phone(brand,model,price,count,version) values(3,3,3,3,3)'

    helper.exec_sql(sql)
