#figure & subplot
"""
subplot()함수사용
"""

from matplotlib import pyplot as plt
import numpy as np
from numpy.random import randn

fig, sp = plt.subplots(2,2)
sp[0,0].plot([2,3,4,5], [81,93,91,97])
sp[0,0].plot(randn(50).cumsum(), 'b--')
