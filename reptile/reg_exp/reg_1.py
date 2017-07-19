import re

print('正则表达式一')

#python用了r之后,就不用字符了,在字符传中也是//待研究

r_1 = r'[0-9a-zA-Z]+@[0-9a-zA-Z]+\.(com|cn|top)'
string_1 = "1647456807@qq.com-"
result_1 = re.match(r_1,string_1)
# print(result_1)
#用match的结果竟然是可以作为flag的,成功match对象失败None,但是,仅仅匹配从开头就能匹配成功的
if result_1:
	# print('匹配成功的字符是:{}'.format(result_1.match)#这个不行,说是没有match选项
	print('匹配成功的位置是:{}'.format(result_1.span()))
else:
	print('匹配失败或者match匹配结果不能做flag')




