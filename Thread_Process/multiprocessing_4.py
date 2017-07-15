#!/usr/bin/python3
#-*- coding:utf-8 -*-

import subprocess

print('子进程的输入')

#感觉这种主要是针对命令行模式的

#这些stdin stdout stderr还是要设定成subprocess.PIPE,否则,直接进入命令行要人手动输入
p = subprocess.Popen(['python'],stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#python命令的话需要print的才是result的
result,err= p.communicate(b'print("this is man life")')
print(result.decode('utf-8'))
print(err.decode('utf-8'))
print('Exit code:', p.returncode)