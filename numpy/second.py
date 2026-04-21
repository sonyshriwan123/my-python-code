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