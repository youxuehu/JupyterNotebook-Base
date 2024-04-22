# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
from keras.utils import to_categorical
from keras import models, layers, regularizers
from keras.optimizers import RMSprop
from keras.datasets import mnist
import matplotlib.pyplot as plt
import time

# 加载数据集
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
print(train_images.shape, test_images.shape)
print(train_images[0])
print(train_labels[0])

print(type(train_images))
print(len(train_images))
# 保存图片
plt.imsave("5.png", train_images[1])
for item in train_images:
    # plt.imshow(train_images[1])
    # plt.imshow(item)
    # plt.show()
    # plt.imsave()
    plt.imsave("%s.png" % str(time.time()), item)
