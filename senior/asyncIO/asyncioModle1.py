import asyncio

async def count():
    print("Count is ready to run...")
    n=0
    while n<50000000:
        n += 1
    print("Count run to the end")
    return "count"

async def delay_one():
    print("delay_one is going ...")
    #await的是一个协程实例对象
    result_one = await count()
    print("delay_one is finished and get {}".format(result_one))
    return "delay_one"
async def delay_two():
    print("delay_two is running...")
    result_two = await asyncio.sleep(4)
    print("delay_two is finished and")
    return "delay_two"

cor_1 = delay_one()
cor_2 = delay_two()

tasks = [
    asyncio.ensure_future(cor_2),
    asyncio.ensure_future(cor_1)
]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
