import numpy as np
print('numpy的通用函数')

# listen very easy just make the function make influence to every element

arr = np.arange(5)
sqrt = np.sqrt(arr)
print(sqrt,sqrt.dtype,sqrt.shape)

#生成8个表征正态分布数字... so many
x = np.random.randn(8)
print(x)
y = np.random.randn(8)
print(y)
max_value = np.maximum(x,y)
print(max_value)

ar_ra = np.array([[1,2,3,4],[3,2,54,7],[8,5,3,2]])
print(ar_ra)
print(np.unique(ar_ra))
print(np.max(ar_ra))
print(np.sum(ar_ra))