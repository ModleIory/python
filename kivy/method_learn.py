import kivy
kivy.require('1.10.1')

print('Some search and learn......')

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.config import Config
from kivy.logger import Logger
from kivy.network.urlrequest import UrlRequest
import urllib.parse
from kivy.animation import Animation


#config deal
'''
Config.set('kivy','log_dir','D:\modle\work\python\kivy\log')
Config.set('kivy','log_enable',1)
Config.set('kivy','log_name','log.log')
Logger.info('begin to run......')
'''

class Interface(GridLayout):
	def __init__(self,**args):
		super(Interface,self).__init__(**args)
		self.rows = 4
		self.orientation = "vertical"
		l = Label(text="this is label")
		self.add_widget(l)
		self.add_widget(Slider(min=0,max=100,value=25))
		self.add_widget(TextInput(text='please input and be silence'))
		self.add_widget(Button(text='This is btn',width=100,height=200))
		#创建动画
		anim = Animation(x=100,y=200)+Animation(x=50,y=-300)
		anim.repeat = True
		animate = lambda *args:anim.start(l)
		Clock.schedule_once(animate,10)
		
#会自动添加些参数
def print_one(*args):
	print('This is print one')

#请求数据get
def get_json(req,result,*args):
	print('***this is get data ****')
	print('get_json得到了数据')
	print(result)
	print(req)
#请求数据post
def post_data(req,result):
	print("***** this is post data ******")
	print(req,result)

class MyApp(App):

	def show(self):
		print('this is show in main')

	def build(self):
		#如果没有数据,默认的就是GET,否则method='GET'
		UrlRequest('https://httpbin.org/headers',get_json,method='GET')
		#post方法
		data = {'@number': 12524, '@type': 'issue','@action': 'show'}
		params = urllib.parse.urlencode(data)
		headers = {'Content-type':'application/x-www-form-urlencoded','Accept':'text/plain'}
		UrlRequest('bugs.python.org',on_success=post_data,req_body=params,req_headers=headers)
		#执行print_one每2秒
		Clock.schedule_interval(print_one,2)
		self.show()
		return Interface()

if __name__ == "__main__":
	MyApp().run()
