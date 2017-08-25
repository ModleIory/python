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

#丢弃索引
print('丢其索引,就是id，不可丢弃字段对于column来说')
wow1 = Series(np.arange(5),index=['a','b','c','d','e'])
print(wow1)
print(wow1.drop(['a','d']))
wow2 = DataFrame(np.arange(9).reshape(3,3),index=['a','b','c'],columns=['num','name','tel'])
print(wow2)
print(wow2.drop(['a','b']))

print('选取索引和过滤series and dataframe')
###Seires
mom = Series(np.arange(4),index=['a','b','c','d'])
print(mom)
#可以用array一样的索引 ， 也可以用key
print(mom[1],mom['b'])
#所以，也就可以用切片饿了
print(mom[1:3],mom['a':'c'])
print(mom[mom<3])
###Dataframe
dad = DataFrame(np.arange(16).reshape(4,4),index=['one','two','three','four'],columns=['1_field','2_field','3_field','4_field'])
print(dad)
print('选择一个field的所有值')
print(dad['1_field'],dad[['1_field','2_field']])
print('现在是选择的是索引了,相当于数据库的条件查询了')
print(dad[:2])
print(dad[dad['4_field']>10])
print(dad<5)
print('ix索引字段，前面的数组是index，后面的而是field')
print(dad.ix[['one','two'],['1_field','2_field']])
print(dad.ix['four',['3_field','4_field']])