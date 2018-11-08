import redis

HOST = '127.0.0.1'
PORT = 6379
DB = 1

pool = redis.ConnectionPool(host=HOST, port=PORT, db=DB)
rds = redis.Redis(connection_pool=pool)

rds.sadd('connect_pool', '连接池连接1','连接池连接2')
