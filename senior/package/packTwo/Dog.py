import sys
sys.path.append("../")
import packOne.Animal

class Dog():
	def __init__(self):
		print("I am dog in two")
	def show(self):
		print("I am show in two")
	def use(self):
		ins = packOne.Animal.Animal()
		ins.show()
dog = Dog()
dog.use()

