import time , threading

print('测试python多线程对变量的影响')
print('在python当中,线程不会像java等一样,会自动利用多个cpu核心,是由于GIL机制')

sum = 1000
t_lock = threading.Lock()
sema = threading.BoundedSemaphore(2)

class test_dirty_var(threading.Thread):
	def __init__(self,n):
		print('to test dirty var')
		self.n = n
		super().__init__()
	def run(self):
		global sum
		global t_lock
		global sema
		for i in range(150000):
			# print('{} and times is {}'.format(self.n,i))
			# 不注释t_lock就会使得结果不一了
			# t_lock.acquire()
			# sema.acquire()
			sum += self.n
			sum -= self.n
			# sema.release()
			# t_lock.release()

one = test_dirty_var(5)
two = test_dirty_var(8)

#如此都是1000
'''
one.start()
one.join()
two.start()
two.join()
print(sum)
'''

#如此不定了
one.start()
two.start()
one.join()
two.join()
print(sum)

#如此摆到最后输出也是会变,不用sleep则直接马上输出1000
'''
one.start()
two.start()
time.sleep(3)
print(sum)
'''

#我推测这个one虽然没有join,但是同时执行的two有join,为了讲究two,必须也是join完了才print
'''
one.start()
two.start()
two.join()
print(sum)
'''


