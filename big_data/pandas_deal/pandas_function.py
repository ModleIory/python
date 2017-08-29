import pandas as pd 
from pandas import Series,DataFrame
import numpy as np

print('函数在pandas数据结构中的应用')

frame = DataFrame(np.random.randn(20).reshape(5,4),index=['a','b','c','e','f'],columns=['one','two','three','four'])
print(frame)

print(np.abs(frame))

max_min = lambda x:x.max()-x.min()

print('列方向的计算和横方向的计算,r然后横竖方向上个输出一个值，依靠的方法是apply')
print(frame.apply(max_min))
print(frame.apply(max_min,axis=1))

print('#'*40)
def deal(x):
	print(x)
	print(type(x))
	print('自动调用每个行列的series进行处理')
print(frame.apply(deal))