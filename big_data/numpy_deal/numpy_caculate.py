import numpy as np
print('numpy array caculate with no circle')

#在这种数组中,不循环就可以计算,不像list一样
print('array的标量的运算,加减乘除直接动,每个都动')
a_1 = [[1,3,4,5],[2,4,6,8],[1,2,2,1]]
arr_1 = np.array(a_1,dtype=np.int16)
# print(arr_1)
arr_1_chen = arr_1*arr_1
arr_1_and = arr_1+arr_1
arr_1_and_ = arr_1+100
arr_1_chu = 5/arr_1
arr_1_chu_ = arr_1/5
# print("+:{},{},*:{},/:{},{}".format(arr_1_and,arr_1_and_,arr_1_chen,arr_1_chu_,arr_1_chu))

print('numpy数组的索引,大同小异的')
print(a_1[0][3],a_1[1][2],a_1[2][3],a_1[0][1:4])#5,6,1,[3,4,5]

#赋值于整个,整个数组无论怎么搞都是关联的,任然在一个数组上操作,是为了大数据的性能考虑
arr_2 = [[1,3],[4,3]]
arr_2_slice = arr_2[0:1]
print(arr_2_slice)
arr_2_slice[0][1]=100
print(arr_2)
#如果是要赋值数组,给两个数组不占据同个内存的话:
arr_origin = [1,3,4,5,6]
new_arr = arr_origin.copy()
print(new_arr)
new_arr[2]=100
print(new_arr)
print(arr_origin)

print('高维数组的索引,似曾相识'+'*'*20)
li_3r = [ [ [1,2,3],[2,34,5] ] ,[ [9,8,19],[12,24,12] ] ]
arr_3r = np.array(li_3r)
#元素索引
print(arr_3r[1,1,2])#12 访问方式可以如此了,不需要arr_3r[1][1][2],当然 返回的只是视图,不是副本 改了原始数组有作用
#切片索引
print(arr_3r[1,1][0:3])
#boolean索引和花式索引...

print('数组的转置和轴对换')
modle = np.arange(16).reshape((4,4))#reshape
print(modle)
#T操作
print(modle.T)
