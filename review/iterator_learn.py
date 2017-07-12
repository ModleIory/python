#!/usr/bin/python3

from collections import Iterable,Iterator

print('Iterator use')

print('判断是否是Iterrable 就是可以用for来循环')

L = []
L_ = isinstance(L,Iterable)
S = (['a'])
S_ = isinstance(S,Iterable)
T = (1,2)
T_ = isinstance(T,Iterable)
D = {'a':'b'}
D_ = isinstance(D,Iterable)

print('list '+str(L_))
print('set '+str(S_))
print('tuple '+str(T_))
print('dic '+str(D_))

print('判断是否是Iterrator,就是可用next的')
def i():
	yield True
	print('first step')
	yield False
	print('second step')
i_ = i()
print('generator function is '+str(isinstance(i_,Iterator)))

L_L = (x+x for x in range(5))
print('generator arr is ' + str(isinstance(L_L,Iterator)))

#iter可以讲[] {} () ([])等Iterable化成Iterator
lister = ['做个好汉子','每天要自强','热血男儿汉','比太阳更广']
iter_lister = iter(lister)
print(next(iter_lister))
print(next(iter_lister))
print(isinstance(iter_lister,Iterator))

