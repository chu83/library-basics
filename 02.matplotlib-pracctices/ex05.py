#figure &subplot
"""
numpy를 이용한 다양한 그래프 그리기
"""

from matplotlib import pyplot as plt
import numpy as np
from numpy.random import randn

fig = plt.figure()
sp1 = fig.add_subplot(2,2,1)
sp2 = fig.add_subplot(2,2,2)
sp3 = fig.add_subplot(2,2,3)
sp4 = fig.add_subplot(2,2,4)


sp1.plot([2,3,4,5], [81,93,91,97])
sp2.plot(randn(50).cumsum(), 'k--')
sp3.hist(randn(100), bins=20, color = 'k', alpha = 0.3)
sp4.scatter(np.arange(100), np.arange(100) + 3*randn(100))
plt.show()