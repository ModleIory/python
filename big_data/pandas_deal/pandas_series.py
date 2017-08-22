import pandas as pd 
from pandas import Series,DataFrame

print('这个Series就像是dict和js中的obj')


print('This is pandas')

#定义序列
print('用数组来定义Series，索引自增')
obj = Series([2,3,4,5,6,[1,2,[3,6]]])
print(obj)
print(obj.values)
print(obj.index)

#自定义索引
print('数组定义series时候的索引自增')
obj2 = Series([2,4,6,8],index=['a','b','c','d'])
print(obj2)

print(obj2[obj2>4])
print(obj2*2)
print('c' in obj2,'e' in obj2)

#也可以用字典来定义
print('用字典来定义series')
dict_ = {'you':'me','our':'us','fight':'struggle'}
obj3 = Series(dict_)
print(obj3)

#还可以替换定义
print('将外部的索引映射进去')
dict_4 = {"one":1,"two":2,"three":3,"four":4}
obj4 = pd.Series(dict_4)
index_arr = ['No.1','one','two']
new_ser = Series(dict_4,index=index_arr)
print(new_ser)

#检测数据是否缺失
print('检测数据是否缺失')
print(pd.isnull(new_ser))
print(pd.notnull(new_ser))

#在运算中，key可以自动对齐,对应的key相加
print('想家key自动找寻，可以修改index的name等等')
all_add = new_ser+obj4
print(all_add)
#这个name不是索引
new_ser.index.name = 'hundred'
new_ser.name = 'You Are Mine'
print(new_ser)
new_ser.index = ['fuck','you','qin']
print(new_ser)