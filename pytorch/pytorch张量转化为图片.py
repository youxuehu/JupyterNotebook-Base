# -*- coding:utf-8 -*-
import torch
from torchvision import transforms
from PIL import Image

# 假设tensor_image是一个PyTorch张量，形状为[3, H, W]
tensor_image = torch.randn(3, 244, 244)  # 示例张量，尺寸为244x244

# 实例化ToPILImage类
to_pil_image = transforms.ToPILImage()

# 将张量转换为PIL图片
pil_image = to_pil_image(tensor_image)

# 显示图片
pil_image.show()