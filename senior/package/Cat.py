import packOne.Animal
import packTwo.Dog

# If I import the document , It is like a obj , I can use method in it.

class Cat():
	def __init__(self):
		print("I am Cat in two")
	def show(self):
		print("I am show in two")
	def useAnimal(self):
		ins = packOne.Animal.Animal()
		ins.show()
	def useWorld(self):
		ins = packOne.Animal.World()
		ins.show()
	def useMethod(self):
		ins = packOne.Animal.showMethod()
cat = Cat()
cat.show()
cat.useAnimal()
cat.useWorld()
cat.useMethod()


