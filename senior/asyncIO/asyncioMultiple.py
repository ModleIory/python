import asyncio
import time

async def delay(second):
    print("Will be delayed {} s".format(second))
    await asyncio.sleep(second)
    return "I am number {} delay".format(second)

cor_1 = delay(1)
cor_2 = delay(2)
cor_3 = delay(3)

# Order is :
# cor_1 first , but meet the delay , so ,hang up and run cor_2
# cor_2 meet delay , hang up and run cor_3 
# cor_3 meet the dalay , no other can run , 
tasks = [
    asyncio.ensure_future(cor_3),
    asyncio.ensure_future(cor_2),
    asyncio.ensure_future(cor_1)
]
loop = asyncio.get_event_loop()
# Here execute the same time , but when the longest app finish would continue
# because output by the order 
loop.run_until_complete(asyncio.wait(tasks))

for task in tasks:
    print(task.result())