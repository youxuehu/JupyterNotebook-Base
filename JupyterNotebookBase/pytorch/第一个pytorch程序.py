# -*- coding:utf-8 -*-
from __future__ import print_function
import torch
# 查看版本
print(torch.__version__)
# tensors 张量
# 矩阵
# 创建无初始化矩阵


# 无初始化
# x = torch.empty(5, 4)
# print(x)
# # 有初始化
# x = torch.rand(5, 4)
# print(x)
#
# x = torch.zero(5, 3, dtype=torch.long)
# print(x)

# x = torch.tensor(
#     [1.1, 2.2]
# )
# print(x)
#
# y = torch.tensor(
#     [1.1, 2.2]
# )
# z = x + y
# print(z.data)

"""
矩阵想加
"""
x = torch.rand(5, 3)
print(x)
y = torch.rand(5, 3)
print(y)

print(x + y)
print(torch.add(x, y))
result = None
print(torch.add(x, y, out=result))
print(result)
# 含义: y = y + x
y.add_(x)

"""
矩阵想减
"""
x = torch.rand(5, 3)
print(x)
y = torch.rand(5, 3)
print(y)

sub_result = None
print(x - y)
print(torch.sub(x, y, out=sub_result))


print(x[:, 1])

