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
frame = DataFrame(data,columns=['number','member','state','more'],index=['one','two','three'])
print(frame)

print('可以将列搞成一个series,就是相同的属性')
print(frame['number'])
print('得到一个个体个全面的属性')
#设定一个field的属性
frame['more'] = 'zhuchangying'
print(frame)
# print(frame.xi.['one'])


