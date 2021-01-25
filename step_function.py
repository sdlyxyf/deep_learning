# @Author : sdlyxyf@163.com
# @File: step_function.py
# @Software : PyCharm
# @Time :2021/1/23 下午11:05

#阶跃函数，输入超过0时输出1，否则输出0

import numpy as np
import matplotlib.pylab as plt


def step_function(x):
    return np.array(x > 0, dtype=np.int)


x = np.arange(-5.0, 5.0, 0.1)
# print(x)
y = step_function(x)
# print(y)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()
