#!/usr/bin/python3
#-*- coding:utf-8 -*-

print('this is generator......')

# If it is list and it is so large , It would waster of time and memory , If I get next by logic

#构造
print('yield构造一')
	#列表构造
L = [x*x for x in range(15)]
print(L)
	#generator构造一
G = (x*x for x in range(15))
print(G)
print(next(G))
print(next(G))
print('*'*30)
#一般都用for循环,不会由于遍历完了报错stopIterrater
for y in G:
	print(y)

	#yield构造二 普通函数中有了yield,那就是generator,每个generator把函数分成了好几次执行,每次就如同list里面的一个值,所谓生成器,就是生成可循环的[]
print('yield构造二')

#原始的函数
def fib(max_times):
	times,a,b = 0,0,1
	while times<max_times:
		a,b = b,a+b
		print(b)
		times += 1

fib(10)

print('yield构造二...yield')
def fib_g(max_times):
	times,a,b = 0,0,1
	while  times<max_times:
		yield str(b)+'fuck'
		a,b = b,a+b
		times += 1
		yield 'end fuck'
	return 'ok !'

# f_g = fib_g(10)
# print(next(f_g))
# print(next(f_g))
# print(next(f_g))
# print(next(f_g))

for x in fib_g(10):
 	print(x)


print('final area......')
R = set([1,3,4,5])
print(type(R),R)
#must是构造的列表形式才可以
Q = (x for x in range(10))
print(Q)

'''
标注:
	有两种形式,只要是在学习的时候,都不可以急躁,速度是建立在高效的基础上而非浮躁
	一种是()的  一种是用函数yield的
'''