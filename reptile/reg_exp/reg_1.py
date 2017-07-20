import re

print('正则表达式一')

#python用了r之后,就不用字符了,在字符传中也是//待研究

r_1 = r'([0-9a-zA-Z]+)@([0-9a-zA-Z]+)\.(com|cn|top)'
string_1 = "1647456807@qq.com-"

result_1 = re.match(r_1,string_1)
# print(result_1)
#用match的结果竟然是可以作为flag的,成功match对象失败None,但是,仅仅匹配从开头就能匹配成功的
if result_1:
	# print('匹配成功的字符是:{}'.format(result_1.match)#这个不行,说是没有match选项
	print('匹配成功的位置是:{}'.format(result_1.span()))
	#匹配成功的部分原来是用group(0)啊
	print(result_1.group(0))
	print(result_1.group(1))
	print(result_1.group(2))
	print(result_1.group(3))
else:
	print('匹配失败或者match匹配结果不能做flag')

print('*'*60)
string_2 = r"_-1647456807@qq.com"
result_2 = re.search(r_1,string_2)
print(result_2)
if result_2:
	print('string2匹配成功')
	print(result_2.span())
	print(result_2.group(0))
	print(result_2.group(1))
	print(result_2.group(2))
	print(result_2.group(3))
else:
	print('匹配失败或者是不能如此判别')

print('*'*60+'切分字符串')
#只要遇到下列的符号就要切分
string_3 = 'a,b,c,;d  ;e'
r_2 = r'[\s,;]'
arr = re.split(r_2,string_3)
print(arr)

print('*'*60+'贪婪和非贪婪匹配')
string_4 = '12011012306'
#这个会完全的匹配
r_3 = r'.+0'
result_3 = re.search(r_3,string_4)
print(result_3)
#在*和+后面加?
r_4 = r'.+?0'
result_4 = re.search(r_4,string_4)
print(result_4)

print('*'*60+'编译和匹配')
#当一个re要使用很多次数的时候,用这种方法,无疑是很有效率的
string_all = ''' <meta charset="utf-8" />
    <title>正则表达式 - 廖雪峰的官方网站</title>
    <meta name="viewport" content="width=device-width" />
    <meta name="keywords" content="javascript,node,jquery,git,python,java,sql,linux,ios,android,教程,软件,编程,开发,运维,云计算,网络,互联网" />
    <meta name="description" content="研究互联网产品和技术，提供原创中文精品教程" />
    <meta property="x-nav" content=" /wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000 " />
    <link rel="alternate" href="/feed" title="廖雪峰的官方网站" type="application/rss+xml" />
    
    <meta property="og:type" content="article" />
    <meta property="og:url" content="http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143193331387014ccd1040c814dee8b2164bb4f064cff000" />
    <meta property="og:title" content="正则表达式" />
    <meta property="og:description" content="小白的Python新手教程，基于最新的Python 3.6！" />
    <meta property="og:image" content="http://www.liaoxuefeng.com/files/attachments/001431608955727f25be118770e460fad1296261e01213d000/l" />'''

r_all = r"content=\"(.+?)\""
r_compile = re.compile(r_all)
#findall返回的是一个数组,而且是正则里面的()里面的部分构成的
result = re.findall(r_compile,string_all)
print(result)











