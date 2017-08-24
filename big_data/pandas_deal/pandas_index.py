from pandas import Series,DataFrame
import  numpy as np
import pandas as pd

print('索引不可以直接改变，但是可以重新定义index值')

print('for series')
arr_value = ['one','two','three','four','five','six']
arr_index = [1,2,3,4,5,6]
s = Series(arr_value,index=arr_index)
print(s)
i = s.index
print(i)
#不能直接修改索引值，报错
# i[1] = 'fuck'
# 重新规定索引，返回一个新的值,若是不存在的索引返回缺失值,除非有fill_value
s_s = s.reindex(['a',4,1,5,'e','f','g'],fill_value='fuck')
print(s_s)

print('for dataframe')
frame = DataFrame(np.arange(9).reshape(3,3),index=np.array(['one','two','three']),columns=['num','name','age'])
print(frame)
new_f = frame.reindex(index=['one','two','three','four'],columns=['num','name','age','sex'],fill_value='0_0')
print(new_f)
