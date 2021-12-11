# -*- coding:utf-8 -*-
import os


current_dir = os.path.dirname(__file__)
print(current_dir)

MY_DEFAULT_STATIC_FILES_PATH = os.path.join(os.path.dirname(__file__), "static")

MY_DEFAULT_TEMPLATE_PATH_LIST = os.path.join(os.path.dirname(__file__), "templates")
