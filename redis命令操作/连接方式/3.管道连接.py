import redis

HOST = '127.0.0.1'
PORT = 6379
DB = 2
pool = redis.ConnectionPool(host=HOST, port=PORT, db=DB)
rds = redis.Redis(connection_pool=pool)
pipe = rds.pipeline()
pipe.set('conn_pip1', '管道连接1')
pipe.set('conn_pip2', '管道连接2')
pipe.execute()
