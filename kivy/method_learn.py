import kivy
kivy.require('1.10.1')

print('Some search and learn......')

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.label import Label
from kivy.uix.slider import Slider

class Interface(GridLayout):
	def __init__(self,**args):
		super(Interface,self).__init__(**args)
		self.cols = 2
		self.add_widget(Label(text="this is label"))
		self.add_widget(Slider(min=0,max=100,value=25))

#会自动添加些参数
def print_one(*args):
	print('This is print one')

class MyApp(App):

	def show(self):
		print('this is show in main')

	def build(self):
		#执行print_one每2秒
		Clock.schedule_interval(print_one,2)
		self.show()
		return Interface()

if __name__ == "__main__":
	MyApp().run()
