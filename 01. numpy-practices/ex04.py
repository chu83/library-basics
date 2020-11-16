import numpy as np

for n in range(10):
    print(n, end=' ')

arr1 = np.arange(10)
print(arr1, arr1.shape, arr1.dtype)

arr1 = np.arange(1,11)
print(arr1, arr1.shape, arr1.dtype)

arr1=np.linspace(10, 15, 6)
print(arr1, arr1.shape, arr1.dtype)