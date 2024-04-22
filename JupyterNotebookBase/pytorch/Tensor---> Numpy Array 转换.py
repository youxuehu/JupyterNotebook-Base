# -*- coding:utf-8 -*-
import torch

# tensor 转换 numpy
x = torch.ones(5)
print(x)

y = x.numpy()
print(y)

x.add_(1)

#  x，y 共享同一个内存变量
print(x)
print(y)

# numpy 转换 tensor
import numpy as np

print(np.__version__)

a = np.ones(5)
print(a)
b = torch.from_numpy(a)
print(b)
