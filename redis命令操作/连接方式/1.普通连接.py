import redis

HOST = '127.0.0.1'
PORT = 6379
DB = 0

rds = redis.Redis(host=HOST, port=PORT, db=DB, decode_responses=True)
rds.set('connect_type', '普通连接')
print(rds.get('connect_type'))
