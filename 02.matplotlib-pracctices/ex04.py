#figure & subplot
"""
크기가 1*2 인 figure 2개의 서브플롯을 추가한 예
"""

from matplotlib import pyplot as plt

fig = plt.figure()
sp1 = fig.add_subplot(1,1,1)
sp2 = fig.add_subplot(1,2,2)

sp1.plot([2,4,5,6], [81,89,33,55])
sp2.plot([1,2,8,7], [4,1,78,3])
plt.show()