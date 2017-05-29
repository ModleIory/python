#!/usr/bin/python3
# -*- coding:utf-8 -*- 

import export


export.one()
export.two()

from export import export 

instance = export("man to stand!")
instance.love()

