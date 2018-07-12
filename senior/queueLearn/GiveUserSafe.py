# 安全的生产者消费者模式==>只要运行的次数足够多，在修改同一个变量，那么，就会出现变量污染
import threading 
import time
import queue

q = queue.Queue(maxsize=5)

class Product(threading.Thread):
    def __init__(self,q):
        super(Product,self).__init__()
    def run(self):
        count = 0
        global num
        while count<20:
            count+=1
            q.put("apple",block=True)
            print("Server has create an apple")
            time.sleep(3)
            pass

class Consumer(threading.Thread):
    def __init__(self,q):
        super(Consumer,self).__init__()
    def run(self):
        global num
        count = 0
        while count<20:
            count+=1
            ele = q.get(block=True)
            print("Client has got an "+ele)
            time.sleep(1)
            pass

# Product(q).start()
# Consumer(q).start()



mixNum = 0
L = threading.Lock()
class NumberChange(threading.Thread):
    def __init__(self,type,lock):
        super(NumberChange,self).__init__()
        self.lock = lock
    def run(self):
        global mixNum
        count = 0
        while count<100000:
            self.lock.acquire()
            if type=="add":
                mixNum+=2
            else:
                mixNum-=1
            self.lock.release()
            count+=1
        print(mixNum)
one = NumberChange('add',L)
two = NumberChange('sub',L)
# one.start()
# two.start()
            
