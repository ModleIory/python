#!/usr/bin/python3
# -*- coding:utf-8 -*- 


from PIL import Image
import os

print('this is pillow lib learn')

path = 'test.png'
sample = Image.open(path)
print('图片的信息是{}'.format(sample))
print(sample.size,sample.mode,sample.format.lower())
#调用外部程序来展示图片
# sample.show()
# 存储图片
# sample.save('fuck.jpg')
# 分离名字和后缀名
#print(os.path.splitext(path))
# print(path.split('.'))

# 缩略图的制作,尺寸和大小都有缩小
'''
new_size = (100,100)
sample.thumbnail(new_size)
sample.save('small.png')
'''

#裁剪图片
box = (50,50,200,220)
region = sample.crop(box)
#下面实际上也不用旋转,只是为了好看在同个图像上复制
# region = region.transpose(Image.ROTATE_180)
# 这个box不可修改,否则报错
#下面的sample可以是个新的对象
'''
sample.paste(region,box)
sample.save('cut_img.png')
'''
#创建一个新画布
new_img = Image.new('RGBA',(300,300),'yellow')
#这里paste,只要box的尺寸一样就好,位置可以变的
new_img.paste(region,box)
# new_img.show()
new_img.save('fuck_you.png')









