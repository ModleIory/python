#!/usr/bin/python3
# -*- coding:utf-8 -*-

import subprocess

print('多进程执行外部程序')

print("想要开个子进程来运行 nslookup www.baidu.com")
r = subprocess.call(['nslookup','www.baidu.com'])
print('exit code :{}'.format(r))
result = subprocess.call(['python','--version'])
print('exit code :{}'.format(result))
