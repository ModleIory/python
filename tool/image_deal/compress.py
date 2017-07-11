#!/usr/bin/python3
#-*- coding:utf-8 -*-

import os
from PIL import Image,ImageFilter

print('python script to deal with pictures......')

path = 'src/test.jpg'

name,ext = os.path.splitext(path)

img_obj = Image.open(path)

size = img_obj.size

#把图像剪切到另一个新图形里面
'''
new_img = Image.new('RGBA',size,'gray')
box = (200,200,600,800)
region = img_obj.crop(box)
new_img.paste(region,(0,0,400,600))
new_img.save('yoxi.jpg')
'''

#压缩图片空间大小
'''
img_obj.thumbnail(size)
img_obj.save('{}_compressed.jpg'.format(name))
'''

#形状上的处理
'''
#resize
img_obj.resize( (size[0]+500,size[1]) ).save('resize.jpg')
#rotate
img_obj.rotate(45).save('rotate.jpg')
'''

#图像过滤
'''
img_obj.filter(ImageFilter.GaussianBlur).save('GaussianBlur.jpg')
# 普通模糊
img_obj.filter(ImageFilter.BLUR).save('BLUR.jpg')
# 边缘增强
img_obj.filter(ImageFilter.EDGE_ENHANCE).save('EDGE_ENHANCE.jpg')
# 找到边缘
img_obj.filter(ImageFilter.FIND_EDGES).save('FIND_EDGES.jpg')
# 浮雕
img_obj.filter(ImageFilter.EMBOSS).save('EMBOSS.jpg')
# 轮廓
img_obj.filter(ImageFilter.CONTOUR).save('CONTOUR.jpg')
# 锐化
img_obj.filter(ImageFilter.SHARPEN).save('SHARPEN.jpg')
# 平滑
img_obj.filter(ImageFilter.SMOOTH).save('SMOOTH.jpg')
# 细节
img_obj.filter(ImageFilter.DETAIL).save('DETAIL.jpg')
'''
