#!/usr/bin/python3
# -*- coding:utf-8 -*-

from multiprocessing import Pool,cpu_count
import os , time ,random

# print('***多进程池子***我的cpu的内核数量是{}'.format(cpu_count()))


def last_time_task(n):
	print('tast {} has is running and self_pid is {} parent_id is {}'.format(n,os.getpid(),os.getppid()))
	time.sleep(2)
	print("No.{} is running".format(n))

if __name__ == "__main__":
	print('Main process pid is {}'.format(os.getpid()))
	#仅仅允许4个进程同时运行,等到第一个完之后,最后一个才开始在这里
	p = Pool( int(cpu_count()) )
	for i in range( int(cpu_count())+1 ):
		p.apply_async(last_time_task,args=(i,))
	#不允许再添加进程了
	p.close()
	p.join()
	print("All is done")

#这两种情况的子进程都是本身



