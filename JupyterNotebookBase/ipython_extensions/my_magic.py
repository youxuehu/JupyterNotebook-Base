# -*- coding:utf-8 -*-
from __future__ import print_function
from IPython.core.magic import Magics, magics_class, line_magic, cell_magic, line_cell_magic


@magics_class
class MyMagics(Magics):
    @line_magic
    def lmagic(self, line):  # 行魔术命令
        "my line magic"
        print("Full access to the main IPython object:", self.shell)  # 可以控制整个ipython内核
        # #整个命名空间的变量
        # #同在ipython中的get_ipython().kernel.shell.user_ns.keys()==get_ipython().user_ns.keys()
        print("Variables in the user namespace:", list(self.shell.user_ns.keys()))
        return line

    @cell_magic
    def cmagic(self, line, cell):
        "my cell magic"
        return line, cell

    @line_cell_magic
    def lcmagic(self, line, cell=None):
        "Magic that works both as %lcmagic and as %%lcmagic"
        if cell is None:
            print("Called as line magic")
            return line
        else:
            print("Called as cell magic")
            return line, cell

    @line_cell_magic
    def hello_hello(self, line):
        "Magic that works both as %lcmagic and as %%lcmagic"
        print("Called as line magic")
        return line
