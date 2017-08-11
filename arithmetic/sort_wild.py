print('野生排序法')

origin = [12,21,58,12,34,56,32,43,12,4,76,234,1,21,43,56]

def wild(arr):
	arr.sort()
	print(arr)
	arr.reverse()
	print(arr)

wild(origin)