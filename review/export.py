#!/usr/bin/python3

def one():
	print('this is one')

def two():
	print('this is two')

class export():
	secret = None
	def __init__(self,secret):
		self.secret = secret
		print('this is class function')
	def love(self):
		print("{} is a great power".format(self.secret))
		