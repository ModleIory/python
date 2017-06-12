# -*- coding:utf-8 -*-
# decorator
def show_love(fn):
	def wrapper():
		print('This world filled with love')
		fn()
	return wrapper


'''
normal
'''
#实际上,被解析成了 one = show_love(one)
@show_love
def one():
	print('Who"s eys is shine')
one()


print('!#?'*30)

def show_hate(fn):
	def wrapper():
		fn()
		print('This world alse filled with hatred')
	return wrapper
		

@show_hate
@show_love
def I():
	print("I am standing here")
I()

print('!#'*30)

##用class来声明decorator
class fighter():
	fn = None
	def __init__(self,func):
		self.fn = func
	def __call__(self):
		print('this is class decorator __call__ method')
		self.fn()

@fighter
def wow():
	print('believe yourself!')
wow()



#被修饰函数带参数的decorator
def deco(fn):
	def wrapper(*argv):
		for x in argv:
			print(x)
			fn()
	return wrapper

@deco
def love(*wo):
	print('this is love in prama')
love('a','b','c','d','e')


#decorator自己带参数
def stubborn(type):
	def middle(func):
		def wrapper(age):
			print('this is tow params docorator')
			if type==True:
				print('is best')
			else:
				print('is wrost!!!!')
			print('age is {}'.format(age))
			func(age)
		return  wrapper
	return middle

@stubborn(True)
def fuck(age):
	print('I an in fuck')

fuck(32)

print("wowowowowowo************"*10)


def shower(position):
	def middle(func):
		def wrapper(argv):
			if position=='header':
				print('this is header')
				func(argv)
			elif position=='footer':
				func(argv)
				print('this is footer')
			else:
				print('position argv is not right!')
		return wrapper
	return middle

@shower('footerl')
def func(name):
	print('this is a function name is {}'.format(name))

func('hello world')
