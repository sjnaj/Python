'''
Author: fengsc
Date: 2022-03-03 18:14:13
LastEditTime: 2022-03-14 15:11:40
'''
from matplotlib import pyplot as plt
import numpy as np
import math
x = np.arange(0, math.pi*2, 0.05)
y = np.sin(x)
fig=plt.figure(facecolor='orange',edgecolor='orange',frameon=True)#新建画布

plt.plot(x,y)
plt.title("sine wave")
plt.xlabel('angle')
plt.ylabel('sine')
plt.show()
