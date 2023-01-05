import numpy as np

arr1 = np.array([2,3,7,9.3])
arr2 = np.array([2,3,5,6.4])
np.set_printoptions(precision=12)
print("Input arrays:") 
print(arr1)
print(arr2)
print("\nThe two arrays are equal (element wise) or not:?")
print(arr1 == arr2)