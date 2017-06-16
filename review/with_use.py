#这个东西实际上就是替代f.close这些关闭操作的,比如锁,线程,文件,就可以省略关闭操作

with open('text.txt','wb') as file:
	content = '这个厨师内容'
	data = file.write(content.encode('utf-8'))
	print(data)