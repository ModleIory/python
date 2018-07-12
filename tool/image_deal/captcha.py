#!/usr/bin/python3
# -*- coding:utf-8 -*-

#验证码生成图片
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random

print('create a captcha......')

name = 'captcha.jpg'
size = (250,80)
bgcolor = random.choice(['yellow','orange','pink','white','green','deepskyblue','hotpink','red'])
line_num_area = (2,5)
line_color = 'red'
point_num_area = (30,100)
#点出现的概率是5%
point_rate = 5
point_color = random.choice(['yellow','orange','pink','white','green','deepskyblue','hotpink','red'])
chars = 'ABCDEFGHJKMNPQRSTUVWXYabcdefghjkmnpqrstuvwxy123456789'
chars_num = 5
font_type = 'arialbi.ttf'
font_size = 45
font_color = random.choice(['blue','gray','black'])

def get_chars(strs,num):
	return random.sample(strs,num)

def create_paper(size,bgcolor):
	paper = Image.new('RGBA',size,bgcolor)
	return paper

def create_line(paper,line_num_tuple,color):
	#这里的*是打开符号
	w,h = paper.size
	line_pen = ImageDraw.Draw(paper)
	line_nums = random.randint(*line_num_tuple)
	for i in range(line_nums):
		begin_point = (random.randint(0,w),random.randint(0,h))
		end_point = (random.randint(0,w),random.randint(0,h))
		line_pen.line([begin_point,end_point],fill=color)
	
def create_point(paper,point_rate,color):
	w,h = paper.size
	point_pen = ImageDraw.Draw(paper)
	#难道不是point_none_rate的数字吗 这里对概率进行计算可以学习下
	chance = min( 100,max( 0,int(point_rate) ) )
	print('chance is {}'.format(chance))
	#开始像粒子一样扫描点
	for w_ in range(w):
		for h_ in range(h):
			tmp = random.randint(0,100)
			#也就是有只有5%的概率才绘制
			if tmp > 100-chance:
				point_pen.point((w_,h_),fill=color)

def create_letter(paper,char_arr,font_type,font_size,font_color):
	letter_pen = ImageDraw.Draw(paper)
	w,h = paper.size
	#将得到的字符串组合成" x x x x "的片段
	char_str = ' {} '.format(' '.join(char_arr))
	font = ImageFont.truetype(font_type,font_size)
	#根据font的设定得到已知字符的宽度高度
	font_w,font_h = font.getsize(char_str)
	# print(w,h,font_w,font_h)
	letter_pen.text( ((w-font_w)/2,(h-font_h)/2 ),char_str,font=font,fill=font_color )





paper = create_paper(size,bgcolor)
create_line(paper,line_num_area,line_color)
create_point(paper,point_rate,point_color)
char_arr = get_chars(chars,chars_num)
create_letter(paper,char_arr,font_type,font_size,font_color)
paper = paper.filter(ImageFilter.EDGE_ENHANCE_MORE)
paper.convert("RGB").save(name)


#get from here
'''
random.choice(['a','b','c'])|random.sample('abcdefj',2)|random.randint(0,10)|打开符号 *(12,34,56)
img = Image.open(src)|Image.new('RGBA',size,color)|img.save()|img.filter()|pen = ImageDraw.Draw(img)|pen.line()|pen.point()...
''.join(list)
'''