import kivy
#改成目前所用的kivy版本号
kivy.require('1.10.1')

from kivy.app import App
#kivy.uix专门是用户的元素的
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout

#how to config Global setting
kivy.kivy_base_dir = 'base_dir'
kivy.kivy_modules_dir = 'modules_dir'
kivy.kivy_data_dir = 'data_dir'
kivy.kivy_icons_dir = 'icon_dir'
kivy.kivy_home_dir = 'home_dir'


#login interface
class LoginTip(GridLayout):
	def __init__(self,**args):
		
		super(LoginTip,self).__init__(**args)

		self.cols = 2
		self.add_widget(Label(text='username'))
		self.add_widget(TextInput(multiline=False))
		self.add_widget(Label(text='password'))
		self.add_widget(TextInput(password=True,multiline=False))
		self.add_widget(Label(text='click for in...'))

class MyApp(App):
	def build(self):
		return LoginTip()

if __name__ == "__main__":
	MyApp().run()


''' first most easy sample
class first(App):
	#build汗水一定要有,是执行的函数
	def build(self):
		return Label(text="hello world ! this is quick start!")

if __name__ == '__main__':
	first().run()
'''