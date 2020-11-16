import numpy as np

#1차원 모든요소가 0인 size 5인 1차원 배열
arr1 = np.zeros(5)
print(arr1, arr1.ndim, arr1.shape)

#2차원 모든요소가 0인 4*3 배열
arr2 =np.zeros((4,3))
print(arr2)

#1차원 모든요소가 1인 size 5인 배열
arr2 = np.ones(5)
print(arr2)

#1차원 모든요소가 3인 size 5인 배열
arr1 = np.full(5,3)
print(arr1, arr1.ndim, arr1.shape)

#2차원 모든요소가 3인 4*3배열
arr2 = np.full((4,3), 3)
print(arr2)