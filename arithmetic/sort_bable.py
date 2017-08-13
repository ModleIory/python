print('这个是冒泡排序法,从小到大的')

origin = [12,21,58,12,34,56,32,43,12,4,76,234,1,21,43,56]

def babel(arr):
	l = len(arr)
	for	j in range(0,l):
		for k in range(j+1,l-j):
			if arr[j]>arr[k]:
				tmp = arr[j]
				arr[j] = arr[k]
				arr[k] = tmp
	print(arr)


babel(origin)