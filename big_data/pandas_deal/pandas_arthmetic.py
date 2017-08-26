import numpy as np 
import pandas as pd 
from pandas import Series,DataFrame

print('about the deal')
print("Series的运算")
s1 = Series([1,2,4,5],index=['a','b','c','d'])
s2 = Series([3,5,6,7,8],index=['a','b','c','d','e'])
print(s1)
s12 = s1+s2
#缺失的值做运算还是缺失
print(s12)
print("DataFrame的运算")
df1 = DataFrame(np.arange(9).reshape(3,3),index=[1,2,3],columns=list('abc'))
df2 = DataFrame(np.arange(20).reshape(5,4),index=[1,2,3,5,6],columns=list('aqcd'))
print(df1)
print(df2)
df12 = df1+df2
print(df12)
#凡是df1有的column，若是Nan，都会填充12345，
df12_add = df1.add(df2,fill_value=12345)
print(df12_add)
print("DataFrame和Series的运算")
print('广播')
arr = np.array([[1,2,3],[2,3,4],[5,6,7]])
print(arr)
arr_0 = np.array([1,2,3])
print(arr_0)
broadcast = arr-arr_0
print(broadcast)
print('减去一行，然后每行都减，就叫广播，dataFrame和series也一样')

ss = Series({'a':1,'b':2,'c':3,'d':4})
dd = DataFrame(np.arange(9).reshape(3,3),index=['one','two','three'],columns=['a','b','c'])
#相减项目匹配的dataFrame的column和series的index
print(ss)
print(dd)
d_s_result = dd-ss
print(d_s_result)




