import pandas
from pandas import Series,DataFrame
import numpy as np 

print("表格型的数据结构")
print('实际上就像是mysql了，在DataFrame当中，key就是相当于field了，其他相应的key对应的array里面，就是多个字段了')

state = np.array(['I am you','you are me ','fight to burst this world'])
member = np.array(['zhangsanfeng','jiaxu','zhongyaji'])
number=  np.array([1,2,3])
data = {
	'state':state,
	'member':member,
	'number':number
}
#这里可以制定顺序呢,将field定制成属性,将index看做table的id
frame = DataFrame(data,columns=['number','member','state','more','more_2'],index=['one','two','three'])
print(frame)

print('可以将列搞成一个series,就是相同的属性')
print(frame['number'])
print('给一个filed的所有赋值')
frame['more'] = 'zhuchangying'
# frame['number'] = 100
print(frame)
print('给列赋值可以动用series,或者nparray') 
frame['more_2'] = np.arange(3)
print(frame)
attach = Series(['loving you','zhongyaji','xixhahaha'],index=['one','two','three'])
frame['more_2'] = attach
print(frame)
print('可为不存在之列赋值，可用del删除列')
frame['more_3'] = np.arange(3)
print(frame)
del frame['more_3']
print(frame)
print('嵌套型字典的成dataform')
obj = {
	"one_field":{
		'1':'you',
		'2':'me'
	},
	"two_field":{
		'1':'zhong',
		'2':'wuruijie'
	}
}
f = DataFrame(obj)
print(f)
print('filed 和 index 进行转置')
print(f.T)
f_ = DataFrame(obj,index=['1','2','3'])
print(f_)
print('得到值')
print(f.values)







