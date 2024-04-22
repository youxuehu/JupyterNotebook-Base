# -*- coding:utf-8 -*-
import torch
import torchvision
import torchvision.transforms as transforms
from torch import nn
from torch.nn import functional as F
from PIL import Image


# 定义模型
class AlexNet(nn.Module):
    def __init__(self, num_classes=10):
        super(AlexNet, self).__init__()
        self.features = nn.Sequential(
            nn.Conv2d(1, 48, kernel_size=11, stride=4, padding=2),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),
            nn.Conv2d(48, 128, kernel_size=5, padding=2),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),
            nn.Conv2d(128, 192, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(192, 192, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(192, 128, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),
        )
        self.classifier = nn.Sequential(
            nn.Dropout(p=0.5),
            nn.Linear(128 * 6 * 6, 2048),
            nn.ReLU(inplace=True),
            nn.Dropout(p=0.5),
            nn.Linear(2048, 2048),
            nn.ReLU(inplace=True),
            nn.Linear(2048, num_classes),
        )

    def forward(self, x):
        x = self.features(x)
        x = torch.flatten(x, start_dim=1)
        x = self.classifier(x)
        return x


# 加载预训练的AlexNet
pretrained_alexnet = torchvision.models.alexnet(pretrained=True)
# 修改最后的全连接层以适应10个类别（0-9）
num_classes = 10
classifier = AlexNet(num_classes).classifier
pretrained_alexnet.classifier = classifier

# 准备数据
transform = transforms.Compose([
    transforms.Grayscale(num_output_channels=1),
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,)) # 平均值和标准差应该根据你的数据集来定
])

# 准备图片
image = "/Users/youxuehu/PycharmProjects/JupyterNotebook-Base/pytorch/搭建手写数字识别/image/1.png"

# 加载图片并预处理
example_image = transform(Image.open(image).convert('L'))
example_image = example_image.unsqueeze(0)  # 添加额外的维度来匹配batch_size

# 进行推理
with torch.no_grad():
    output = pretrained_alexnet(example_image)
    predicted_idx = torch.argmax(output, dim=1).item()
    print(f"The predicted digit is: {predicted_idx}")

# 确保你已经安装了Pillow库，用于图像处理