import numpy as np

arr1 = np.array([[2,3,4],[1,2,3]])
arr2 = np.array([[5,6,7],[2,4,6]])
print("Array1:")
print(arr1)
print("Array2:")
print(arr2)
print("\nMultiply arrays of same size element-by-element:")
print(np.multiply(arr1, arr2))