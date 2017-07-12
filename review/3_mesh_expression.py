
one = 230
two = 100

print('三元操作符号')
state = "one is bigger" if one>two else "two is bigger"
print(state)

print('#列表生成表达式')
L = [x+'oo' for x in ['a','b','c','d']]
print(L)

#about the link compare链式比较
n = 10
flag = 1<n<11
print(flag)

print('list赋值')
l = ['about','your']
a,b = l
print(a,b)

print('字典生成用for')
dic = {x:x*x for x in range(10)}
print(dic)

print('枚举的演练')
ll = ['长路漫漫','人生','林子祥']
for i,k in enumerate(ll):
	print(str(i)+" => "+k)

print('方法返回多个值')
def wow():
	return 'me','you','ha'
a,b,c = wow()
print(a,b,c)

print('使用打开运算符号*来布置函数参数')
var = [1,2,3]
def mom(a,b,c):
	return a*a,b*b,c*c
print(mom(*var))
