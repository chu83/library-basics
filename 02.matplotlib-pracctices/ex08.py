#figure & subplot
"""
subplot()함수 사용
추가옵션 사용
sharex : 서브플롯이 x축 눈금을 함께 쓴다.
sharey : 서브플롯이 u축 눈금을 함께 쓴다.

"""

from matplotlib import pyplot as plt
import numpy as np
from numpy.random import randn
"""
fig, sp = plt.subplots(2, 2, sharex=True, sharey=True)
for i in range(2):
    for j in range(2):
        sp[i,j].hist(randn(100), color='r', alpha=0.3)

plt.subplots_adjust(wspace = 0, hspace=0)
plt.show()

"""

fig, sp = plt.subplots(1,1)
sp.plot([10,20,30,40], label='data1')
sp.plot([54,78,21,65], label='data2')
plt.legend(loc='best')
plt.show()