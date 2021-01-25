# @Author : sdlyxyf@163.com
# @File: perceptron_demo.py
# @Software : PyCharm
# @Time :2021/1/23 下午10:35

#感知机，神经元节点的学习，实现与门、与非门、或门、异或门
#与门、与非门、或门是一层感知机，异或门是2层感知机

import numpy as np


def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def NOR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.2
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y


if __name__ == '__main__':
    print(AND(0, 0), AND(0, 1), AND(1, 0), AND(1, 1))
    print(NAND(0, 0), NAND(0, 1), NAND(1, 0), NAND(1, 1))
    print(OR(0, 0), OR(0, 1), OR(1, 0), OR(1, 1))
    print(NOR(0, 0), NOR(0, 1), NOR(1, 0), NOR(1, 1))
    print(XOR(0, 0), XOR(0, 1), XOR(1, 0), XOR(1, 1))
