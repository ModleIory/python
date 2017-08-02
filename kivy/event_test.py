import kivy
kivy.require('1.10.1')

print('Especially for kivy event deal')

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App
#这个相当于div,基本都要有
from kivy.uix.gridlayout import GridLayout
from functools import partial
from kivy.uix.widget import Widget

#注册事件
class MyWidget(Widget):
    def __init__(self, *args):
        super(MyWidget, self).__init__(*args)
        #这里注册了事件名字是这个以后,下面的几个也要相同
        self.register_event_type('on_fuck')

    def on_fuck(self,*args):
        print('on_fuck事件出发时候执行这儿')
#这个是自定义的触发事件后的回调函数
def on_fuck_callback(*args):
    print('my fuck is called', *args)
w = MyWidget()


class Demo(GridLayout):
    def __init__(self,*args):
        #这里面的super是自己这个class
        super(Demo,self).__init__(*args)

        self.cols = 4
        self.orientation = 'vertical'
        btn_1 = Button(text='this is button one')
        btn_1.bind(on_press=self.show)
        #LABAL不可以绑定事件
        btn_2 = Button(text='this is button two')
        #这个state事件就是按下去或者放起来都有反应
        btn_2.bind(state=self.show)
        label_1 = Label(text="this is label one")
        label_1.bind(on_press=self.show)
        btn_3 = Button(text='this is button three')
        btn_3.fbind('on_press',self.params_callback,'wuruijie','zhongyaji')
        self.add_widget(btn_1)
        self.add_widget(btn_2)
        self.add_widget(label_1)
        self.add_widget(btn_3)
    def params_callback(self,*args):
        print(args)
        print("my name is {} and your name is {}".format('me',"you"))
    def show(self,*args):
        print("I am clicked!!!")
        #dispatch是触发事件的
        w.dispatch('on_fuck','wowo')

class Main(App):
    def build(self):
        #监听事件
        w.fbind('on_fuck',on_fuck_callback)
        return Demo()

if __name__ == "__main__":
    Main().run()
