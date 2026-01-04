import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
#
# # print(arr.shape)
# newArr = arr.reshape(3,1,4) # x1 * x2 * x3 ....xn = arr.shape
# print(newArr)

# iteration:

# arr2 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]) # [1,2,3,4,5,6,7,8]
#
# for x in np.nditer(arr2):
#     print(x)
#
#
# arr3 = np.array([1,2,3])
#
# for x in np.nditer(arr3,flags = ["buffered"] , op_dtypes = ["S"]):
#     print(x)
# print(arr3[0])
#
#
# arr4 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
#
# for x,y in np.ndenumerate(arr4):
#     print(x,y)

# concatenation:
# print("\nConcatenation: ")
# arr5a = np.array([1,2,3,4,5])
# arr5b = np.array([6,7,8,9,10])
# arr5 = np.concatenate((arr5a,arr5b))
# print(arr5)
#
# arr6a = np.array([[1, 2,4], [3, 4,-4]])
#
# arr6b = np.array([[5, 6,-1], [7, 8,-5]])
# arr6 = np.concatenate((arr6a,arr6b),axis =0)
# print(arr6)
#
#
# arr7a = np.array([1, 2, 3])
#
# arr7b = np.array([4, 5, 6])
# print("\nStacking :")
# arr7 =  np.dstack((arr7a,arr7b))
# print(arr7)

# splitting:

arr8= np.array([1,2,3,4,5,6])
newArr = np.array_split(arr8,2)
print(newArr)

arr9 = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newArr2 = np.array_split(arr9,2)
print(newArr2)

