#!/usr/bin/python3

def in_():
	f = open('text.txt','w+')
	s= 'abcdefg'
	print(s,end='',file=f)
	f.close()
in_()
