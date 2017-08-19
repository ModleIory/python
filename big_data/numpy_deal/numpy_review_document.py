import numpy as np 

print('This is review document!')

#create
'''
l = [[1,2,3,4],[2,3,4,5]]
_l_ = np.array(l)
print(_l_,_l_.dtype,_l_.shape)
a = np.array(10)
print('a:{}'.format(a))
b = np.array( (2,3) ,dtype=np.int32)
print('b:{}'.format(b))
c = np.zeros(5)
print('c:{}'.format(c))
d = np.zeros((2,3))
print('d:{}'.format(d))
e = np.zeros_like(l)
print('e:{}'.format(e))
'''
#caculate
#Of course , use the number is also ok!
x = np.array([[1,2,3],[2,3,4]])
y = np.array([[3,4,5],[5,6,7]])
z = x+y
print(z)
o = x*y
print(o)
p = x/y
print(p)
q = x-y
print(q)
arr_4r = np.arange(20).reshape((4,5))
print(arr_4r)
#索引
print(arr_4r[2,4])