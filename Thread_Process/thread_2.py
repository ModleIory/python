import threading
import time 

print('add join to wait son to end')

class thread_create(threading.Thread):
	def __init__(self,n):
		super().__init__()
		self.n = n
	def run(self):
		print("task",self.n,threading.current_thread())    #输出当前的线程
		time.sleep(1)
		print('3s')
		time.sleep(1)
		print('2s')
		time.sleep(1)
		print('1s')

start = time.time()

t_obj = []

for x in range(3):
	th = thread_create(x)
	th.start()
	th.join()#join在这里就是此个线程完了,在执行下一个线程
	t_obj.append(th)

# for tmp in t_obj:
	# tmp.join()#使得所有子线陈同步执行,完了再来主线程
# t_obj[1].join()

print('delta = {}'.format(time.time()-start))
print('Main thread is {}'.format(threading.current_thread))
print('this is main')
		