#python的函数的操作完全和js一样嘛 什么赋值,变量等等的
#python中的函数嘛,就是像个变量一样嘛
def one():
	print('I am one')
one()
#函数的赋值
two = one
two()

def three(func,name):
	if name==1:
		one()
	elif name==0:
		two()
	else:
		func()
	def inner():
		print('I am inner')
	#可以返回
	return inner

def other():
	print('i am other')

ins = three(name=0,func=other)
ins()

#python要是的函数是一个变量,那么只能像js一样了
one_ = eval('one')
one_()

eval('two()')



print('不定长参数--tuple')
def fun(*more):
	print(more)
fun('you','me','wow')
print('不定长参数--dict')
def func(**ques):
	print(ques)
func(a=1,b=2,c=2)
