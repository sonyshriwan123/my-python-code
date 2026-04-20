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


arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
newarr = arr.reshape(-2)
print(newarr)