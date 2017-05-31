#!/usr/bin/python3
# -*- coding:utf-8 -*- 

import export,sys


print(sys.path)

export.one()
export.two()

from export import export 

instance = export("man to stand!")
instance.love()

