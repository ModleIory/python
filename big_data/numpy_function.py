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
