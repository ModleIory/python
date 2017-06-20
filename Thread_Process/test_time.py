import threading
import time

def run(n):
    global num
    num += 1

num = 0
t_obj = [] 

for i in range(20000):
    t = threading.Thread(target=run, args=("t-%s" % i,))
    t.start()
    t_obj.append(t)

time.sleep(3)
print(num)