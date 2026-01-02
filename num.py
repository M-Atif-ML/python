import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# print(arr.shape)
newArr = arr.reshape(3,1,4) # x1 * x2 * x3 ....xn = arr.shape
print(newArr)

