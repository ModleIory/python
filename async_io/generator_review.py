
def fuck(time):
	count = 1
	while time<5:
		count += 1
		yield count*count
		print('{} times is ok'.format(count))

f = fuck(1)
#每次执行到yield返回yeild后的值,然后停止往下执行
print(next(f))
print(next(f))
print(next(f))
		
		