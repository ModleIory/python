#!/usr/bin/python3
# -*- coding:utf-8 -*-
# 

import time

timestamp = time.time()
print('timestamp is {}'.format(timestamp))

localtime = time.localtime(timestamp)
print(localtime)

asciitime = time.asctime(localtime)
print(asciitime)

mytime = time.strftime("%Y-%m-%d %H:%M:%S",localtime)
print(mytime)

backtime = time.mktime(time.strptime(mytime,"%Y-%m-%d %H:%M:%S"))
print(backtime)
