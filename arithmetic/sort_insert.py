print('这个是插入排序法')

origin = [23,45,21,98,54,12,43,43,1,76,46,54,34,64]

newest = []
tmp = None
for item in origin:
	if not newest:
		print('新的数组是空的......')
		newest.append(item)
	else:
		print('items {}'.format(item))
		tmp = newest[:]
		for index,value in enumerate(tmp):
			if value>=item:
				print(item)
				print(newest)
				newest.insert(index,item)


print(newest)


