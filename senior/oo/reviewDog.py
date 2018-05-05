from reviewAnimal import Animal
class Dog(Animal):
	def __init__(self):
		print("this is Dog")
		#execute parent constructor
		super(Dog,self).__init__()
	def eat(self):
		super().eat()
		print("Dog like eating bones")
	def run(self):
		print("Dog run very fast")
	# multistatus achieve by param , python没有申明的类型,实例化时候也不像java一样有类型,所以,只能若此
	def multiStatusRun(self,obj):
		obj.run()

dog = Dog()
dog.eat()
dog.show()
# 看是否实例--继承的子同时属于父类和自己
print(isinstance(dog,Dog))
print(isinstance(dog,Animal))
# 多态的调用
dog.multiStatusRun(Dog())
dog.multiStatusRun(Animal())

