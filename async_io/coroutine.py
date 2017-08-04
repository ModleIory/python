import time

print('这个是协程,是单线程的')

#这个是会中断的
def product(c):
	#这个是开启
	c.send(None)
	command = 0
	while command<5:
		time.sleep(2)
		command += 1
		print('[生产者]又下达了一条命令{}'.format(command))
		reply = c.send('命令是:{}'.format(command))
		print('[生产者]收到了恢复:{}'.format(reply))
	c.close()


#这个每次执行都是执行完再yield返回 得到倒是及时得到 它不会中断
def consumer():
	r = ''
	while True:
		#自己会马上执行,但是返回去的数据是有延迟的
		# time.sleep(3)
		#注意这个不是马上返回,而是整个函数执行完了 把结果返回 不然不对了 之所以写在这里是为了得到n
		n = yield r
		if not n:
			return 
		print('[消费者]得到了命令{}'.format(n))
		r = 'GET OK２００'

c = consumer()
product(c)

