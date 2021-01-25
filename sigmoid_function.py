# @Author : sdlyxyf@163.com
# @File: sigmoid_function.py
# @Software : PyCharm
# @Time :2021/1/23 下午11:38

import numpy as np
import matplotlib.pylab as plt

#激活函数，1/(1+e^(-x))
def sigmoid(x):
    return 1/(1+np.exp(-x))

#激活函数,输入小于等于0时，输出0，输入大于0时，直接输出该值。
def relu(x):
    return np.maximum(0,x)

x = np.arange(-5.0, 5.0, 0.1)
# print(x)
y = sigmoid(x)
#y=relu(x)
#y=np.sin(x)
# print(y)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()