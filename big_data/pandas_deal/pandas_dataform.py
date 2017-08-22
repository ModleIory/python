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
#这里可以制定顺序呢
frame = DataFrame(data,columns=['number','member','state'])
print(frame)

print('可以将列搞成一个series')
print(frame['number'])


