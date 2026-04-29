# copy and view======

import numpy as np

# arr = np.array([1,2,3,4,5,])
# x = arr.copy()
# arr[0] = 42
# # this is the copy of the arrys
# print(arr)
# # this is the original arrys
# print(x)


# arr2 = np.array([1,2,3,4,5,])
# # x is the view of arr2, it shares the same data
# x = arr2.view()
# arr2[0] = 42

# print(arr2)

# print(x)

# arr = np.array([[1,2,3,4],[6,7,8,9]])
# print(arr.shape)


# arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
# newarr = arr.reshape(4,5)
# print(newarr)
# print(newarr.ndim)


# arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
# newarr = arr.reshape(-2)
# print(newarr)

# ==iterating though a numpy array===
# arr = np.array([[[1,2,3], [4,5,6],[7,8,9,],[10,11,12,]]])
# for x in arr:
#     for y in x:
#         for z in y:
#             print(z)
            
# arr = np.array([[[1,2,3], [4,5,6],[7,8,9,],[10,11,12]]])
# for x in np.nditer(arr):
#     print(x)


# join the two arrays
# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])
# arr3 = np.concatenate((arr1,arr2))
# print(arr3)

# arr4 = np.array([[1,2,3],[4,5,6]])
# arr5 = np.array([[7,8,9],[10,11,12]])
# arr6 = np.concatenate((arr4,arr5), axis=1)
# print(arr6)
# arr4 = np.array([[1,2,3],[4,5,6]])
# arr5 = np.array([[7,8,9],[10,11,12]])
# arr6 = np.concatenate((arr4,arr5), axis=0)
# print(arr6)

# splitting the array
# arr = np.array([1,2,3,4,5,6])
# newarr = np.array_split(arr,2)
# print(newarr)
# arr = np.array([1,2,3,4,5,6])
# newarr = np.array_split(arr,3)
# print(newarr)

# arr = np.array([1, 2, 3, 4, 5, 6])

# newarr = np.array_split(arr, 3)

# print(newarr[0])
# print(newarr[1])
# print(newarr[2]) 

# ===searching arrys======
# arr = np.array([1,2,3,4,5,6,7,8,9,10])
# x = np.where(arr == 4)
# print(x)

# arr = np.array([10, 14, 93, 41, 8, 7])

# x = np.where(arr%2 == 0)

# print(x)


# =======normal=
# x = [1,2,3,4]
# y = [5,6,7,8]
# z = []
# for i ,j in zip(x,y):
#     z.append(i+j)
# print(z)

# # ==========with ufunc====
# x = [1,2,3,4]
# y = [5,6,7,8]
# z = np.add(x,y)
# print(z)   

# def myadd(x,y,z):
#     return x+y+z
# xyz = np.frompyfunc(myadd,3,1)
# print(xyz([1,2,3,4,5],[5,6,7,8,9],[10,11,12,13,14])) 
# print(type(np.add))


# print(type(np.subtract))
# if type(np.subtract) == np.ufunc:
#     print("subtract is ufunc")
# else:
#     print("subtract is not ufunc")


# ========dicision=====
# arr1 = np.array([1,2,3,4,5,6])
# arr2 = np.array([29,34,45,67,48,27])

# newarr = np.divide(arr1,arr2)
# print("Division is:", newarr)
# print(type(np.divide))


# # =====subtract=
# arr1 = np.array([1,2,3,4,5,6])
# arr2 = np.array([29,34,45,67,48,27])

# newarr = np.subtract(arr1,arr2)
# print("subtract is:", newarr)
# print(type(np.subtract))


# # ===multiplication==
# arr1 = np.array([1,2,3,4,5,6])
# arr2 = np.array([29,34,45,67,48,27])

# newarr = np.multiply(arr1,arr2)
# print("multiplication is:", newarr)
# print(type(np.multiply))




#====power==

# arr1 = np.array([1,2,3,4,5,6])
# arr2 = np.array([1,2,3,4,5,6])

# newarr = np.power(arr1,arr2)
# print("power is:", newarr)
# print(type(np.power))


# ===mod/ remeinder
# arr1 = np.array([1,12,35,39,26,31])
# arr2 = np.array([2,4,6,7,11,9])

# newarr = np.mod(arr1,arr2)
# print("Reneinder is:", newarr)
# print(type(np.mod))

# mod/ quotient
# arr1 = np.array([10, 20, 30, 40, 50, 60])
# arr2 = np.array([3, 7, 9, 8, 2, 33])

# newarr = np.divmod(arr1, arr2)

# print(newarr)

# arr = np.array([-1, -2, 1, 2, 3, -4])

# newarr = np.absolute(arr)

# print(newarr)






# x = "Ayush"
# print(type(x))


    