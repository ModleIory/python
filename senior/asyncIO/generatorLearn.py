# If I need a big list and think about the memory,I'd use generator ,It create when I use
# generator can "return" multiple times so If I need return arr please use this 
# There are two methods to create it

# list create format
li = [m+n for m in "wrj" for n in "zyj"]
print(li)

# Define method one : change the [] to () , I can get the generator
gen = (x*x for x in range(0,10))
print(gen)
# generator for each
print(next(gen))
print(next(gen))
for x in gen:
    print(x)

# Define method two:with yield
# yield would return a value and interrupt the process 
def testYield():
    print("one...")
    yield 1
    print("two...")
    yield 2
    print("three...")
    yield 3
    print("four...")
    yield 4
t = testYield()
print(next(t))
print(next(t))
for x in t:
    print(x)

# Iterable & Iterator
# Iterable only can use for 
# Iterator not only can use for ,but also use generator
# iter can transform iterable to iterrator
l = [1,3,4,5,6,8]
it = iter(l)
print(next(it))

# to return number*number         
def returnSquare(num):
    for x in range(num,10):
        yield x*x
result = returnSquare(5)
# for x in result:
#     print(x)
print(next(result))
print(next(result))
# close the iterator
result.close()
print(next(result))


