import random

'''
TIPS: 
0. 就是一个函数如调用生成器generator,和其沟通信息
1. 主要函数(tillNumRun)必须开始send一个None过去作为连接r=r.send(None),然后中断函数(getRandom)处理
2. 当中断函数(getRandom)接受到connect,那么,用 recv = yield count,意思是接受到主要函数的传递的值是recv,然后运行完给主要函数传递的参数是count
3. 当中断函数(getRandom)运行完(必须是运行完),然后,回到主要函数,讲count赋值给1中r,然后继续往下执行
'''
# 需求,随机一个数(0-9),直到出现了9,才继续,和js的ajax一致
# 这个函数的原则就是一个生成器函数嘛
def getRandom():
    count = 0
    recv = yield count    
    while True:
        if not recv:
            return 
        num = random.randint(0,9);
        print("random number is {}".format(num))
        print("message from tillNumRun is {}".format(recv))
        count += 1
        if num==9:
            yield count
        print("end of generator")
def tillNumRun(r):
    # connect start at first I must send a None here to build connection
    # per time send will run the random once 
    r.send(None)
    # connect end
    print("Will run till I got the num I want")
    recv = r.send("Msg from tillNumRun")
    print("I already get the goal number and times is {}".format(recv))
    next(r)
    r.close()
r = getRandom()
tillNumRun(r)





'''
# Liao Xuefeng 教程
def consumer():
    r = ''
    while True:
        # 传送r , 接受作为n
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'
def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        # 传送n , 接受作为r
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()
c = consumer()
produce(c)
'''