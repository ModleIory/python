#!/usr/bin/python3
#-*- coding:utf-8 -*-

#麻皮 ,这里的queue是要小写的
import queue,time,threading,random,sys

def wait(s):
	time.sleep(s)

goods = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
count = 0

print('FIFO队列')
q = queue.Queue(maxsize=10)
print("现在的对了长度是:"+str(q.qsize()))

class creater(threading.Thread):
	def __init__(self,s):
		self.s = s
		super().__init__()
		print('我要开始生产了...')
	def run(self):
		while True:
			g = random.choice(goods)
			print('已经生产出来一个产品{},下一个产品要稍后3s'.format(g))
			q.put(g,block=True)
			global count
			count += 1
			wait(self.s)
			if count>=10:
				sys.exit()

class consumer(threading.Thread):
	def __init__(self,s):
		self.s = s
		super().__init__()
		print('准备开始购买了...')
	def run(self):
		while True:
			print('排队购买到了{},下一个还在生产'.format(q.get(block=True)))
			global count
			wait(self.s)
			if count>=10:
				sys.exit()

#1s生产一个
creater_ = creater(1)
wait(2)
#2s生产一个
consumer_ = consumer(3)
creater_.start()
consumer_.start()
creater_.join()
consumer_.join()

print('All have finished!')

			





