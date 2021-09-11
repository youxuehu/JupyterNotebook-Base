# -*- coding:utf-8 -*-
from nbconvert.preprocessors.execute import ExecutePreprocessor
from traitlets.traitlets import Unicode

error_raise = False


class TigerPreprocessor(ExecutePreprocessor):

    cell_source = Unicode(default_value="pwd", allow_none=False, help="cell source").tag(config=True)

    def preprocess(self, nb, resources=None, km=None):
        print("================TigerPreprocessor=============preprocess============================================")
        super(TigerPreprocessor, self).preprocess(nb, resources, km)

    def preprocess_cell(self, cell, resources, index):
        print("================TigerPreprocessor=============preprocess_cell=========================================")
        super(TigerPreprocessor, self).preprocess_cell(cell, resources, index)


print("=====================tiger_preprocessor.py=========================")