import numpy as np

# 1.实现了很多方法
# 2.性能更好,c实现
# 3.其中每个元素类型必然相同
# 4.更加像list的增强版本

############ 
###构造和类型(dtype)
############
# 基础构造方法==> 其中每个元素类型必须相同
# ndmin 构造array的最小维度
# dtype 数组所需要的数据类型
print("*"*30)
dt = np.dtype(np.int8)
print(dt)
arr = np.array([[1,2,3],[2,3,4],[3,4,5]],ndmin=2,dtype=dt)#规定了每个数组里面的基本元素都是int8,而且,只是是2维度的
print(arr)
print(arr[0][0])

print("*"*30)
dt_struct_one = np.dtype([('age',np.int32)])
print(dt_struct_one)
arr_one = np.array([(12,),(16,),(18,),(2,),(6,),(1,)],dtype=dt_struct_one)#每个数组中的基本元素的格式要像dt_struct_one中的一样
print(arr_one)
print(arr_one[1][0])

# 感觉规定一个元素格式的,如上面两个,那么,多少维度都可以用,如果规定具体格式的如下,那么,仅仅只能够用于严格格式
print("*"*30)
# int8 = i1 int16 = i2 int32 = i4
# b(boolean) i(int) u(unsiged int) f(float) O(python Obj) S(string)
dt_struct_two = np.dtype([("name","S20"),("age","i1"),("marks","f4")])
print(dt_struct_two)
arr_two = np.array([("wuruijie",24,149.5),("zhongyaji",24,159.0),("kuaito",24,600.0)],dtype=dt_struct_two)
print(arr_two)

############ 
### 一些方法和操作和属性
############
# shape
shape_arr = arr.shape
print(shape_arr)
shape_arr_two = np.array([[1,2],[2,3],[4,5]])
print(shape_arr_two.shape)
shape_arr_two.shape = (2,3)#可以改变shape
print(shape_arr_two)
#reshape 这个维度可以有很多维度
shape_arr_three = np.array([[1,2,3,4],[4,5,3,2],[5,7,4,2]])
print(shape_arr_three.shape)
shape_arr_three_transform = shape_arr_three.reshape(2,2,3)
print(shape_arr_three_transform)
# arange
a = np.arange(24)
print(a)
b = a.reshape(2,2,2,3)
print(b)
# ndim 多少维数组
print(b.ndim)

# empty zero
zero = np.zeros((2,2,2),dtype=np.int32,order='C')
print(zero)
one = np.ones((3,3))
print(one)
print(one.dtype)
empty = np.empty((2,3),dtype="S")
print(empty)
print(empty.dtype)

# sum max min std mean
np_one = np.array([2,4,6,8,10],dtype="float32")
print(np_one.mean())
print(np_one.max())
print(np_one.min())
print(np_one.sum())
print("*"*30)
np_two = np.array([[2,4,6],[1,3,5]])
print(np_two.sum())
print(np_two.max())

# 运算
# 一维的很简单的,就是各个元素相对应位置的处理,但是要相对应
count_one = np.array([1,2,3])
count_two = np.array([2,4,6])
one_two_add = count_one+count_two
print(one_two_add*2)
one_two_x = count_one*count_two
print(one_two_x)

# 二维的 维度和个数一直就行
print(one_two_add*2)
count_2one = np.array([count_one,count_two])
count_2two = np.array([count_two,count_one])
print(count_2one)
print(count_2two)
print("*"*30)
print(count_2one+count_2two)

# 切片


