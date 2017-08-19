import numpy as np

print('可以将数组以二进制的形式保存在文件中')


'''保存得到单个数组
arr = np.array(['you','me','love',1,2,3,4,5,4,2])
np.save('helper/array_save',arr)

tmp = np.load('helper/array_save.npy')
print(tmp)
'''

'''保存得到多个数组
a = np.array([[1,2,3,4],[2,3,4,5]])
b = np.array([1,2,3,4,5,6,67,8])
arr_z = np.savez('helper/more_array_save',a=a,b=b)

tmps = np.load('helper/more_array_save.npz')
print(tmps['a'])
print(tmps['b'])
'''

