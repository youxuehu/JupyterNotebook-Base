# -*- coding:utf-8 -*-
"""
模型训练
"""

import os
import torch
import torch.nn as nn
import torch.utils.data as Data
import torchvision
import sys

sys.path.append("搭建手写数字识别")
from model import MyCnn

print(MyCnn)


def train(dir_path):
    print("the gpu is available")
    print(torch.cuda.is_available())
    print("let us go run!")
    EPOCH = 1
    BATCH_SIZE = 50
    LR = 0.001
    DOWNLOAD_MNIST = True

    data_dir = os.path.join(dir_path, "mist")
    train_data = torchvision.datasets.MNIST(root=data_dir, train=True, transform=torchvision.transforms.ToTensor(), download=DOWNLOAD_MNIST)
    train_loader = Data.DataLoader(dataset=train_data, batch_size=BATCH_SIZE, shuffle=True)

    test_data = torchvision.datasets.MNIST(root=data_dir, train=True)

    # Tensor on GPU
    # test_x = torch.unsqueeze(test_data.test_data, dim=1).type(torch.FloatTensor)[:2000].cuda() / 255.
    # test_y = test_data.test_labels[:2000].cuda()

    # Tensor on CPU, 删除 .cuda()
    test_x = torch.unsqueeze(test_data.test_data, dim=1).type(torch.FloatTensor)[:2000] / 255.
    test_y = test_data.test_labels[:2000]

    cnn = MyCnn()

    # cpu 删除这行
    # cnn.cuda()

    optimizer = torch.optim.Adam(cnn.parameters(), lr=LR)
    loss_func = nn.CrossEntropyLoss()

    for epoch in range(EPOCH):
        for step, (x,y) in enumerate(train_loader):
            # CPU 删除这行
            # b_x = x.cuda()
            # b_y = y.cuda()

            # CPU 版本代码, 删除 .cuda()
            b_x = x
            b_y = y

            output = cnn(b_x)
            LOSS = loss_func(output, b_y)
            optimizer.zero_grad()
            LOSS.backward()
            optimizer.step()

            if step % 50 == 0:
                test_output = cnn(test_x)
                # pred_y = torch.max(test_output, 1)[1].cuda().data
                pred_y = torch.max(test_output, 1)[1].data

                accuracy = torch.sum(pred_y == test_y).type(torch.FloatTensor) / test_y.size(0)
                print("Epoch: ", epoch, "| train LOSS: %.4f" % LOSS.data.cpu().numpy(), "| test accuracy: %.2f" % accuracy)

    test_output = cnn(test_x[:10])
    # GPU
    # pred_y = torch.max(test_output, 1)[1].cuda().data
    #CPU
    pred_y = torch.max(test_output, 1)[1].data

    print(pred_y, "prediction number")
    print(test_y[:10], "real number")

    save_dir = os.path.join(dir_path, "checkpoint")
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    torch.save(
        {
            "model_state_dict": cnn.state_dict(),
            "optimizer_state_dict": optimizer.state_dict(),
            "LOSS": LOSS
        }, os.path.join(save_dir, "model.pt")
    )


if __name__ == "__main__":
    train("./")
