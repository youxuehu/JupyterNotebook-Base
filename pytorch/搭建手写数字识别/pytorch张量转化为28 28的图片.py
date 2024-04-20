# -*- coding:utf-8 -*-
import torch
from torchvision.transforms import ToPILImage, Resize, ToTensor
import matplotlib.pyplot as plt

# 假设tensor_image是一个PyTorch张量，形状为(C, H, W)
tensor_image = torch.randn(3, 28, 28)  # 示例张量

# 转换为PIL图片
to_pil_image = ToPILImage()
pil_image = to_pil_image(tensor_image)

# 将PIL图片转换为28x28大小
resize_transform = Resize(28, max_size=28)
resized_image = resize_transform(pil_image)
print(resized_image)
print(type(resized_image))
help(resized_image)
# # 如果需要，将PIL图片转换回PyTorch张量
# to_tensor = ToTensor()
# resized_tensor_image = to_tensor(resized_image)
# print(resized_tensor_image.__dict__)
# print(help(resized_tensor_image))
# print(resized_tensor_image.logdet())