import pickle

dic = {"name":"bob","age":"23"}

#这个要在命令行运行才好,不然都是创建在root目录

with open("./pickle.txt",'wb') as file:
    pickle.dump(dic,file)
    print("Variable save successfully!")

# with open("pickle.txt",'rb') as file:
#     var = pickle.load(file)
#     print(var)

