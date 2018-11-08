import redis

'''
1.普通连接
2.连接池连接
3.管道连接（事务）
'''
HOST='127.0.0.1'
PORT=6379
DB=0
# 设置密码
# 默认数据库显示2进制的数据库，设置True在控制台能看到中文，否则显示二进制数据

# rds=redis命令操作.Redis(host=HOST,port=PORT,db=DB,decode_responses=True)
# rds.set('ok','酷狗')
#
pool=redis.ConnectionPool(host=HOST,port=PORT)
rds=redis.Redis(connection_pool=pool)
rds.sadd('set_name','a','b')
print(rds.smembers('set_name'))
# # 连接池(推荐）
# pool=redis命令操作.Connection(host=HOST,port=PORT,db=DB,decode_responses=True)
# rds=redis命令操作.Redis(connection_pool=pool)

# 管道
# pool=redis命令操作.Connection(host=HOST,port=PORT,db=DB,decode_responses=True)
# rds=redis命令操作.Redis(connection_pool=pool)
# pipe=rds.pipeline()
# pipe.set('1','一号')
# pipe.set('2','二号')
# pipe.set('3','三号')
# pipe.execute()

