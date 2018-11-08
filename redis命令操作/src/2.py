import redis

HOST='127.0.0.1'
PORT=6379
DB=0

pool=redis.Connection(host=HOST,port=PORT,db=DB,decode_responses=True)
rds=redis.Redis(connection_pool=pool)

'''
name 键
value 表示值
ex=None,   过期时间 单位秒
px=None,    过期时间 单位毫秒
nx=False,   如果设置为True 表示当key不存在的时候才去设置值，存在就不不设置值
xx=False    如果设置为True 表示name存在的时候才去设置值
'''
rds.set('py',1805,ex=10)
rds.set('nx1', 'nx的作用',ex=1*60,nx=True)
rds.set('nx1', '修改已存在的值',ex=2*60,nx=True)

rds.setex('k1','v1',20)
rds.setnx()

dic={
    'k1':1,
    'k2':2
}
rds.mset(dic)
#等价
rds.mset(k1=1,k2=2)
# 获取值
# print(rds.get('k1'))同时获取多个值
print(rds.mget('k1','k2'))

#二进制位操作
rds.setbit('k3',4,1)
# 签到功能
rds.bitcount('k3')


'''
name 键
start  统计1的开始索引位置
end  统计1结束的索引位置
'''

#自增 ,点赞功能
'''
name 键
amount + 1

'''
rds.incr('uid:1:msg:10')
rds.incr('uid:1:msg:10')

#往name对应的值后面追加内容
rds.append('k3','hehe')