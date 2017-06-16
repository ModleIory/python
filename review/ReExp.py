import re
print('regular expresss')

rule = r'(http://)?(www\.)?\w*\.(\w){3}'

url1 = "http://www.qq.com"
url2 = "http://qq.com"
url3 = 'qq.com'

#match从字符串的开始匹配,开始要匹配到正则规则完才会返回,如果不是,就返回None
result1 = re.match(rule,url1+'fuk')
print(result1)
print(result1.group())
print(result1.group(1))
print(result1.group(2))
print(result1.group(3))

#search返回第一个成功的
result2 = re.search(rule,'deal'+url1+'fuck you ')
print(result2)
#group()实际上是返回匹配成功的部分
print(result2.group())
#group(index) 是返回匹配的字表达式
print(result2.group(1))

#sub替换字符串
string = "I am man for play , I love play most "
pattern = r"play"
out = re.sub(pattern,'work',string,1)
print(out)

#移除数字的内容
str_ing = '地址:我日马屁 0878-1212120'
pa = r'\d+-\d+'
final = re.sub(pa,'点击查看电话号码',str_ing)
print(final)

#先编译在匹配
print('先编译在匹配')
rule = r'\d'
r = re.compile(rule)
print(r)
stringi = '12146546'
end = re.search(r,stringi)
print(end)