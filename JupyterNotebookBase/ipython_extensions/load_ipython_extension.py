# -*- coding:utf-8 -*-
from JupyterNotebookBase.ipython_extensions.my_magic import MyMagics


def load_ipython_extension(ipython):
    ipython.register_magics(MyMagics)
