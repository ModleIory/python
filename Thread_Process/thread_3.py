import threading
import time

print('count the son threading number')

class son_thread(threading.Thread):
	def __init__(self,n):
		super().__init__()
		self.n = n
	def run(self):
		print('this is thread {}'.format(self.n))
		time.sleep(1)
		print('come to end')

t_one = son_thread('one')
t_two = son_thread('two')
t_one.start()
t_two.start()

time.sleep(0.5)

print(threading.active_count())
