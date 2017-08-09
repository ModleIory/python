
L = ['modle','sherlock','your','mine']
#一个是复制了数组 ,一个是换个变量 任然指向那个地址
O = L
P = L[:]
# O.pop()
P.pop()

for i,v in enumerate(L):
	print(i,v)