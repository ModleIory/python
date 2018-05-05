import types
class student():
    #限定允许拓展的属性,方法,没有规定就增加不上,报错的
    __slots__ = ("name","getAge","age")
    def __init__(self):
        pass
s = student()

# 给实体增加属性,仅仅是这个实体
s.name='wuruijie'
print(s.name)
#给实体加方法,仅仅这个实体
def getAgeIn(self,age):
    print("Have set age to {}".format(age))
    self.age = age
s.getAge = types.MethodType(getAgeIn,s)
# 这个语法是对的,但是vscode的lint 不识别
#s.getAge(24)
#print(s.age)
