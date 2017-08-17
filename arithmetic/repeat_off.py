print('python 去重')

l = [1,2,3,4,3,2,3,4,5,3,23,2,1,3,34,54,5,34,3,2,1,1,1,1]

#最简单的方法用set的不重复属性
# print(set(list))

#从这里可以知道遍历数组,记住的是下标
# for k,v in enumerate(l):
# 	tmp = l.pop(0)
# 	print(k,v)

#推出一个,然后循环和原来中的对比,同的设定成None,不导致其索引不对,然后推入新数组
'''
def get_rid_one(arr):
	new_arr = []
	while arr:
		ele = arr.pop(0)
		if ele:
			new_arr.append(ele)
		# print(arr)
		for k,v in enumerate(arr):
			print('ele是{},v是{}'.format(ele,v))
			if v==ele:
				#删除了使得index不对,所以删不对
				arr[k] = None
	return new_arr
print(get_rid(l))
'''

#
def get_rid_two(arr):
	new_arr = []
	arr.sort()
	# print(arr)
	tmp = None
	while arr:
		ele = arr.pop(0)
		#记录前一个的值
		if tmp != ele:
			# print('fuck')
			new_arr.append(ele)
		tmp = ele
	return new_arr


print(get_rid_two(l))
