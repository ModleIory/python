import os

print('python is a kind of "glue language" so , use it ')
print('就是当做胶水把其他语言程序结合应用起来')

#这个是等于把结果全部写入docuemnt在读出来结果
print(os.popen('ping qq.com'))
f = os.popen('ping qq.com')
f_ = f.read()
print(f_)

#这个是慢慢的模拟执行  返回值的0|1
print(os.system('ping qq.com'))