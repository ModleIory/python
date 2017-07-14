#!/usr/bin/python3
# -*- coding:utf-8 -*-

print('map redcue all is function and sequence relationship')
#map把一个iterable[for可用]放入一个函数处理生成一个iterator[next]
L = ['one','two','three']
def deal_l(ele):
	return ele+ele
L_ = map(deal_l,L)
print(list(L_))

from functools import reduce
#reduce就是像是递归一样,两个参数,每次的结果和下个参数一起继续计算
def get_sum(x,y):
	return x+y
L = [1,2,3,4,5,6,7]
sum = reduce(get_sum,L)
print(sum)

#filter也是function(one)和list,function必须根据list的元素返回true或者false来决定,结果也是iterator
LL = [1,2,3,4,5,6,7,8,9,0]
def filt(x):
	return x%3 == 2

LL_ = filter(filt,LL)
print(list(LL_))

#sort


