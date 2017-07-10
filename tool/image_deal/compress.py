#!/usr/bin/python3
#-*- coding:utf-8 -*-

import os
from PIL import Image

print('python script to compress pictures......')

path = 'src/test.jpg'

name,ext = os.path.splitext(path)

img_obj = Image.open(path)

img_obj.save("{}.png".format(name))