# -*- coding:utf-8 -*-
from notebook.base.handlers import IPythonHandler  # noqa
import psutil  # noqa
from pexpect import replwrap  # noqa
import json
from tornado import gen, web
try:
    from jupyter_client.jsonutil import json_default
except ImportError:
    from jupyter_client.jsonutil import (
        date_default as json_default
    )
from notebook.utils import maybe_future
from JupyterNotebookBase.utils.json_utils import dumps
import torch
import sys
sys.path.append("pytorch/搭建手写数字识别")
from model import MyCnn
from interferenve import MnistClassifyService
import cv2


class NumHandler(IPythonHandler):

    @web.authenticated
    @gen.coroutine
    def post(self):
        """
        http://localhost:9999/getNum
        :param kernel_id:
        :return:
        """
        self.log.info("NumHandler")
        # 检查是否有文件上传
        file_info = self.request.files['file'][0]  # 'file' 是表单中的input的name属性值
        filename = file_info['filename']
        data = file_info['body']

        # 将文件数据写入服务器
        with open(filename, 'wb') as f:
            f.write(data)

        self.write("File uploaded successfully: " + filename)

        checkpoint = torch.load("./checkpoint/model.pt")
        mnist = MnistClassifyService(checkpoint["model_state_dict"], False)
        # print(cv2.imread)
        image = cv2.imread("image/0.png", 0)
        # print(image.shape)
        print("你输入的数字是：%s" % str(mnist.classify(image)))

        self.finish(json.dumps(res, default=json_default))


default_handlers = [
    (r"/getNum", NumHandler),
]
