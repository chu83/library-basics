#2차원 배열 조회
import numpy as np

arr1 = np.array([[1,2,3,4,5],[10, 20, 30, 40, 50]])

print(arr1.size, arr1.shape)

row, col = arr1.shape

for r in range(row):
    for c in range(col):
        print(f'arr1[{r}][{c}] : {arr1[r][c]}')