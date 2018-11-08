import redis

HOST = '127.0.0.1'
PORT = 6379
DB = 1

pool = redis.ConnectionPool(host=HOST, port=PORT, db=DB)
rds = redis.Redis(connection_pool=pool)

rds.mset(name='a',password='123')
# rds.mget({'name':'a','password':'123'})
rds.mset({"name":'a', "password":'123'})