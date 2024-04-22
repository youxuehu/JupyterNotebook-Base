# -*- coding:utf-8 -*-
import torch
import sys
sys.path.append("搭建手写数字识别")
from model import MyCnn
import cv2


class MnistClassifyService(object):
    def __init__(self, state_dict=None, is_cuda=False):
        if not state_dict:
            raise ValueError("state_dict 不能为空")
        self.is_cuda = is_cuda
        self.model = MyCnn()
        if is_cuda:
            self.model.cuda()
        self.model.load_state_dict(state_dict)
        self.model.eval()

    def classify(self, image):
        h, w = image.shape
        x = torch.from_numpy(image).type(torch.FloatTensor) / 255
        x = x.view(1, 1, h, w)
        if self.is_cuda:
            x = x.cuda()
        y = self.model(x)
        pred_y = torch.max(y, 1)[1].cpu().numpy()
        return pred_y[0]


if __name__ == "__main__":
    checkpoint = torch.load("./checkpoint/model.pt")
    mnist = MnistClassifyService(checkpoint["model_state_dict"], False)
    # print(cv2.imread)
    image = cv2.imread("image/0.png", 0)
    # print(image.shape)
    print("你输入的数字是：%s" % str(mnist.classify(image)))
