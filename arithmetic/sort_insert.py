print('这个是插入排序法,从小到大的')

origin = [23,45,21,98,54,12,43,43,1,76,46,54,34,64]
def deal(arr):
	#从第二的index开始处理,依次和左边的的对比,小于左边就换位置
	length = len(arr)
	for i in range(1,length):
		#PYTHON中的方法不能够像是js中一样可以链式调用!只能一步一步来index = list(range(0,i)).reverse()不可!
		index = list(range(0,i))
		#这个reverse是反转数组,然后,不返回,只能输出原数组
		# index.reverse()
		#遍历的方向也要正确,从左到右,从最小到最大遍历才成立
		for j in index:
			#从大到小或者从小到大的决定
			if arr[j]>arr[i]:
				tmp = arr[j]
				arr[j] = arr[i]
				arr[i] = tmp
	print(arr)




deal(origin)
