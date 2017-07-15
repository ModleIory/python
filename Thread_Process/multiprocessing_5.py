#!/usr/bin/python3
#-*- coding:utf-8 -*- 

from multiprocessing import Process,Queue
import os ,time ,random

print('进程之间的通信')

def write(q):
	L = ['A','B','C','D']
	for x in L:
		q.put(x)
		print('已经推入了{},下一轮上架即将开始'.format(x))
		time.sleep(2)

def read(q):
	while  True:
		value = q.get(True)
		print('拿到了{},等待下一个生产...'.format(value))

if __name__ == '__main__':
	q = Queue()
	pw = Process(target=write,args=(q,))
	pr = Process(target=read,args=(q,))
	pw.start()
	pr.start()
	pw.join()
	pr.terminate()
	print('所有的东西都已经上架完了.....')


#Queue用于进程之间的共享数据的,应该多了解Queue这个玩意儿