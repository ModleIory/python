#!/usr/bin/python3
# -*- coding:utf-8 -*-

#需求,在执行前,欢迎语句,执行后,结束语
def state(func):
    def wrap(argv):
        print("Welcome to you !")
        func(argv)
        print("Good Bye")
    return wrap

#需求,在执行时候,根据函数情况,进行输出信息
def showType(func):
    def wrap(argv):
        print("Your id type is {}".format(argv))
        func(argv)
    return wrap

# 需求,在执行时候,根据装饰器参数,输入不同后果
def filter(type):
    def func(func):
        def param(argv):
            if type=="man":
                print("Strong and stubborn!")
                func(argv)
                print("man is end!")
            elif type=='woman':
                print("Soft and kind!")
                func(argv)
                print("woman is end!")
            else:
                print("What the fuck you are?")
                func(argv)
                print("Fuck is end!")
        return param
    return func

# 装饰器的执行是逐层往外的
@state
@showType
@filter("woman")
def addNum(argv):
    print("*"*80)
addNum("Manager")

