#!/usr/bin/python3
# -*- coding:utf-8 -*-

import os#这个的fork只能够在mac和linux使用
from multiprocessing import Process#这个才是跨平台的

# print('python的多进程')

# print('主进程的pid是:{}'.format(os.getpid()))

'''只能在unix上
p_id = os.fork()

if p_id == 0:
	print('*'+这是子进程)
	print('子进程,父进程pid是{},子进程pid是{}'.format(os.getpid(),os.getppid()))
	print('*'+这是子进程结束)
else:
	print("父进程{}创建了子进程{}".format(os.getpid()),p_id)
'''

#定义方法看起来和Process有点像

def statement(flag):
	print('开始跑进程名字是{},主进程pid是{}'.format(flag,os.getpid()))

if __name__ == "__main__":
	#没创建一个新的process就会重新刷新主进程因为主进程的pid会变
	p_1 = Process(target=statement,args=('one',))
	# p_2 = Process(target=statement,args=('two',))
	p_1.start()
	p_1.join()#用于进程的同步的
	# p_2.start()
	# p_2.join() 
	print('all the process is over')