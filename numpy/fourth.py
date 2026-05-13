import numpy as np
# ==addition===
# arr1 = np.array([1,2,3,4])
# arr2 = np.array([5,6,7,8])
# newarr = np.add(arr1,arr2)
# print("Addition is", newarr)

# ====summation
# arr1 = np.array([1,2,3])
# arr2 = np.array([5,6,7])
# newarr1 = np.sum([arr1,arr2])
# print("Summation is", newarr1)

# cumulative summation=====
# arr = np.array([1,2,3,4,5,6])
# newarr = np.cumsum(arr)
# print("Cumlative summation is", newarr)


# ==product====30/04/2026
# arr = np.array([1,2,3,4,5,6])
# x = np.prod(arr)
# print("The Product is :", x)

# product to using two array===
# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])
# x = np.prod([arr1,arr2])
# print("The Product is:",x)



# ======two array is using prod() axis
# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])
# x = np.prod([arr1,arr2], axis=1)
# print("The Product is:",x)


# cumulative product()
# arr3 = np.array([1,2,3])
# x = np.cumprod(arr3)
# print("The Cumulative product is:", x)




































# import pandas as pd
# l = [14,15,96,99,87]  #create data 
# ds = pd.Series(l)
# print(ds)
# print(ds[4])


# ds = pd.Series()
# print(ds)


# l = [14,15.3,96,99,87] # change data type of element by implicit type convserion
# ds = pd.Series(l)
# print(ds)

# data = [1,2,3,4,5,6]
# s = pd.DataFrame(data)
# print(s)
# data = [{'a':1, 'b' : 2}{'a' : 5, 'b': 14,c': 10}]
# df = pd.DataFrame(Data)
# print(df)

# data = {'Name':['Tom', 'steve','Ricky','rohan', 'sohan'],
#        'age':[20,25,24,26,30],
#        'salary': [20000,45000,85000,45000,32000]}
# df =pd.DataFrame(data)
# # print(df)
# # print(df.head())
# # print(df.tail())
# # print(df.colums)
# # print(df.shape)
# # print(df.rename(columns={'salary' : 'Monthly Salary'},inplace=True))
# # print(df)

# # a =df.describe()
# # print(a)

# # df.info()
# df.to_csv("xyz.txt")
# # df.to_csv("xyz.txt",index=False)
# # a.to_csv("describe.txt")
