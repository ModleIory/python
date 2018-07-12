import queue

print("This will show how to use queue")

# FIFO queue
fifoQueue = queue.Queue(maxsize=5) #maxsize=5 队列中只有5个任务，如果没有被消费，那么只能陷入阻塞
fifoQueueEmpty = fifoQueue.empty()
print("目前的队列是否为空：")
print(fifoQueueEmpty)
i=0
while i<5:
    fifoQueue.put(i,block=True,timeout=2) # put_nowait() 直接推入，如果满了直接报错
    i+=1
fifoQueueFull = fifoQueue.full()
print("当前的队列是否满了：")
print(fifoQueue.full())
print("目前队列的元素个数：")
print(fifoQueue.qsize())
print("得到元素")
print(fifoQueue.get())
print(fifoQueue.get())
print("目前队列的元素个数：")
print(fifoQueue.qsize())
print(fifoQueue.get(block=True,timeout=2)) #如果没有元素，那么等待2秒
print(fifoQueue.get(block=False)) #相当于get_nowait() 没有了就直接报错了
print(fifoQueue.get())
print("没有元素了，等待4s，如果还是没有就直接报错了")
print(fifoQueue.get(block=True,timeout=4))
