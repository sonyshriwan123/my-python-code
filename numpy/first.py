# import numpy

# arr = numpy.array([1, 2, 3, 4, 5])

# print(arr)

import numpy as np

# arr = np.array([1, 2, 3, 4, 5])

# print(arr)

# print(type(arr))
# ===0D==========
# arr = np.array(42)

# print(arr)


# ===1D========
# arr = np.array([1, 2, 3, 4, 5])

# print(arr)

# ====2D====
# arr = np.array([[1, 2, 3], [4, 5, 6]])

# print(arr)
# ===3D==
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# print(arr)

# higher di arrays==

# arr = np.array([1, 2, 3, 4], ndmin=5)

# print(arr)
# print('number of dimensions :', arr.ndim)
# ===indexing=====

# arr = np.array([1, 2, 3, 4])

# print(arr[0])

# arr = np.array([1, 2, 3, 4])

# print(arr[2] + arr[3])
# 
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# print(arr[0, 1, 2])
# ===1D array====

# array = np.array([1,2,3,4,5,6])
# print(array[0])

# ==== 2D arrays
# array_2D = np.array([[1,2,3],[4,5,6]])
# print(array_2D[0,1])


# =====3Darrays
# array_3D = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
# print(array_3D[0,2,1])


# ===slicing the arrays==
# 1D arrays
# array = np.array([1,2,3,4,5,6])
# print(array[1:4])

# 2D arrays==
array_2D = np.array([[1,2,3],[4,5,6]])
print(array_2D[0:2,1:3])
