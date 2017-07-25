#!/usr/bin/python3
#-*- coding:utf-8 -*-

import time

print('get_poem and get_guwen main thread')
print('***            ***')
print('\n')
print('    _________    ')
print('      ____    ')

import thread_get_1,thread_get_2
guwen = thread_get_1.get_guwen()
gushi = thread_get_2.get_author()
gushi.start()
print('先开始得到古诗了,三秒后,古文也开始得到')
time.sleep(3)
guwen.start()
print('古诗也开始得到的过程中了')
gushi.join()
guwen.join()

print('所有的得玩了')
