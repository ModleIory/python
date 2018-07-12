# 不安全的生产者消费者模式==>只要运行的次数足够多，在修改同一个变量，那么，就会出现变量污染
import threading 
import time

queue = []
num = 0

class Product(threading.Thread):
    def __init__(self):
        super(Product,self).__init__()
    def run(self):
        count = 0
        global num
        while count<1000000:
            # print("Product created one element")
            queue.append(1)
            count += 1
            num +=2
        print(len(queue))
        print("the product : "+str(num))

class Consumer(threading.Thread):
    def __init__(self):
        super(Consumer,self).__init__()
    def run(self):
        count = 0
        global num
        while count<1000000:
            # print("Consumer took one element ")
            queue.pop()
            count += 1
            num +=1
        print(len(queue))
        print("the consumer : "+str(num))


Product().start()
Consumer().start()