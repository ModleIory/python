import pandas as pd

# pandas比于numpy方法更多
# pandas是list和collection


# Series 索引数组,像php的array了
pd_one = pd.Series([1,2,3])
print(pd_one)
print("*"*50)
#还可以规定索引
pd_two = pd.Series(["one","two","three"],index=["good","ok","moon"])
print(pd_two)
print(pd_two['good'])
print(pd_two[0])

print("*"*100)
# DataFrame ==>Like dictionary=>Its output is like a sql table,里面每项的元素长度一样长
pd_three = pd.DataFrame({
    "name":['modle','jack','micheal'],
    "age":[12,23,12]
})
print(pd_three)
print(pd_three['name'][0])

pd_four = pd.DataFrame([[1,2],[3,4]])
print(pd_four)

pd_five = pd.DataFrame({
    "user":[{"name":"me","age":23},{"name":"she","age":20}],
    "address":[{"city":"chuxiong","addr":"zixizhen"},{"city":"chuxiong","addr":"qixianglu"}]
})
print(pd_five)