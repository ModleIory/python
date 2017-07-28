import os
#setting environment variable like this

# os.environ['KIVY_NO_CONSOLELOG'] = '1'#是否显示console日志,只要赋值一个str就会有作用
os.environ['KIVY_USE_DEFAULTCONFIG'] = '1'#启动制定的日志
os.environ['KIVY_HOME'] = '/config.ini'#配置文件
# os.environ['KIVY_DATA_DIR'] = '/data'
# os.environ['KIVY_MODULES_DIR'] = '/module'
#这里面的kivy都要小写
import kivy
#改成目前所用的kivy版本号
kivy.require('1.10.1')

from kivy.app import App
#kivy.uix专门是用户的元素的
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout

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