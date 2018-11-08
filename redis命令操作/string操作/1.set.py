import redis

HOST = '127.0.0.1'
PORT = 6379
DB = 1

pool = redis.ConnectionPool(host=HOST, port=PORT, db=DB)
rds = redis.Redis(connection_pool=pool)

# rds.set('name','ex',ex=5)
# rds.set('name','px',px=5000)
# a=rds.set('name','px',px=5000,nx=True)
rds.set('name','tom')
