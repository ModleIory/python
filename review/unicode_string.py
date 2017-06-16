#!/usr/bin/python3
#! -*- coding:utf-8 -*-


print('About python string')
#unicode把世界上所有的语言统一到了一套编码里面,而python的编码就是unicode,最全面的,但是对于a,b,c这些有点浪费,于是,就使用utf-8,自动节俭空间,ascii仅仅对于english
#所以常用的编码有 utf-8 gbk ascii 在encode()参数中

print(ord('A'))
print(ord('啊'))
print(chr(65))
print(chr(23654))

#python的str在内存中是unicode表示的,要是存储或者传输的话,要改变成bytes形式
#abc和b'abc'不一样,abc是str,而后面的是每个字符只占用一个字节,unicode转化为了utf8,对于英文也就是ascii了
x = b'abc'
print(x)

#可以用encode来转化编码
print('AVB'.encode('utf-8'))
print('AVB'.encode('ascii'))

china = "中国"
print(china.encode('utf-8'))
print(china.encode('gbk'))
try:
	print(china.encode('ascii'))
except Exception as e:
	print(e)
print('#'*30)

#以为utf-8是中英文通用的,所以,要用它来作为中间者来转化
print(u'哈哈')

print('*'*20+'code open file')

# f = open('text.txt','rb')
# content = f.read()
#r模式打开
# print(type(content.encode))
# print(type(content.encode('utf-8')))
# print(content.encode('gbk'))
#rb模式
# print(content)
# print(content.decode('gbk'))

# f.close()

file = open('text.txt','wb')
ha = "有着我也由着你真爱永不死"
ha_bytes = ha.encode('utf-8')
print(ha_bytes)
file.write(ha_bytes)
file.flush()
file.close()

