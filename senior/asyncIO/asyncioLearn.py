import asyncio
import threading
import time

# async定义协程,一个协程coroutine对象,不能直接运行,要加入时间循环运行
'''
Step:
1. define coroutine function
2. run the function and get coroutine object
3. create loop event
4. create task
5. run the task
'''

######## 如果仅仅用这个例子的话,那么实际作用也是不大的
# execute and would get a coroutine object 
async def doSomeThing(state):
    time.sleep(state)
    print("Waiting : {}".format(state)) 
    # The reply will send to the callback parameters
    return "doSomeThing"

# give a future object
def callback(future):
    print("I am callback...... I got msg from coroutine is {}".format(future.result()))

cor = doSomeThing(2)
loop = asyncio.get_event_loop()
# when create task , I become a future object
task = asyncio.ensure_future(cor)
task.add_done_callback(callback)
loop.run_until_complete(task)
print("I am from end of function msg: {}".format(task.result()))






'''
# yield的send至少一样多才行
# review old knowledge
def test():
    # here the delay is not useful , run print directly!!
    asyncio.sleep(3)
    print("ok!")
# test()

def gen():
    yield "Link ok!"
    #正式回应
    result = yield "Who?"
    print(result) # Tim
    result = yield "Bye!"
    print(result)
def main(c):
    #建立连接
    result = c.send(None)
    print(result) # Link ok!
    #正式开始
    result = c.send("Tim")
    print(result) # Who
    result = c.send("Bye!")
    print(result)

c = gen()
main(c)
'''




