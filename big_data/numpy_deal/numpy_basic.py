import numpy as np
print('numpy basic learning...')

######create ndarray by change list
#list支持的式样,numpy不一定支持,因为他是做向量和矩阵的运算的
l = [[1,3,4],[2,3,6]]
# l = [1,2,3,4,2,1,3]
# l = [[1,2,3,6,3],2,1,5,[1,3],'s',['s','c']]
l_np = np.array(l)
#shape是显示维度和每个维度的个数
print('the array is {} and shape is {} and dtype is {} and type is {}'.format(l_np,l_np.shape,l_np.dtype,type(l_np)))

######create ndarray by original way
m = np.zeros(5)
print(m)
m = np.zeros((5,6))
print(m)
print(m.shape,m.dtype)

print(np.ones(4))
print(np.ones((2,2)))
print((np.ones_like(m)))

print(np.empty(10))

print(np.arange(10))#0~10
print(np.arange(5,10))#5~10
print(np.arange(5,20,2))#5~10 step is 2

###### create ndarray and use dtype
#int it the array is not the dimension but the sequence
x = np.array((1,2,3),dtype=np.float16)
print( x )
#转换type,是创建一个新数组了
x1 = x.astype(np.int16)
print(x1)




