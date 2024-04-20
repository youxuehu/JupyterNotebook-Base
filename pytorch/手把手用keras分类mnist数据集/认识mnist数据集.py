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
plt.imsave("5.png", train_images[1])
for item in train_images:
    # plt.imshow(train_images[1])
    # plt.imshow(item)
    # plt.show()
    # plt.imsave()
    plt.imsave("%s.png" % str(time.time()), item)


#将图片由二维铺开成一维

train_images = train_images.reshape((60000, 28*28)).astype('float')
test_images = test_images.reshape((10000, 28*28)).astype('float')
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)


# 二、搭建一个神经网络
network = models.Sequential()
network.add(layers.Dense(units=15, activation='relu', input_shape=(28*28, ),))
network.add(layers.Dense(units=10, activation='softmax'))


# 三、神经网络训练
# 1、编译：确定优化器和损失函数等

# 编译步骤
network.compile(optimizer=RMSprop(lr=0.001), loss='categorical_crossentropy', metrics=['accuracy'])


# 2、训练网络：确定训练的数据、训练的轮数和每次训练的样本数等

# 训练网络，用fit函数, epochs表示训练多少个回合， batch_size表示每次训练给多大的数据
network.fit(train_images, train_labels, epochs=20, batch_size=128, verbose=2)


# 四、用训练好的模型进行预测，并在测试集上做出评价

# 来在测试集上测试一下模型的性能吧
y_pre = network.predict(test_images[:5])
print("y_pre")
print(y_pre, test_labels[:5])
test_loss, test_accuracy = network.evaluate(test_images, test_labels)
print("test_loss:", test_loss, "    test_accuracy:", test_accuracy)


