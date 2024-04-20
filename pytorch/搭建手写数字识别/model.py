# -*- coding:utf-8 -*-
"""
准备模型
"""
import torch.nn as nn  # noqa


class MyCnn(nn.Module):

    def __init__(self):
        """
        __init__
        """
        super(MyCnn, self).__init__()
        self.conv1 = nn.Sequential(
            nn.Conv2d(in_channels=1, out_channels=16, kernel_size=5, stride=1, padding=2),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2)
        )
        self.conv2 = nn.Sequential(nn.Conv2d(16, 32, 5, 1, 2), nn.ReLU(), nn.MaxPool2d(2))
        self.out = nn.Linear(32 * 7 * 7, 10)

    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = x.view(x.size(0), -1)
        return self.out(x)


if __name__ == "__main__":
    model = MyCnn()
    stat_dic = model.state_dict()
    print(stat_dic)
