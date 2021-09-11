# -*- coding:utf-8 -*-
from nbconvert.preprocessors.execute import ExecutePreprocessor
from traitlets.traitlets import Unicode

error_raise = False


class TigerPreprocessorV2(ExecutePreprocessor):

    cell_source = Unicode(default_value="pwd", allow_none=False, help="cell source").tag(config=True)

    def preprocess(self, nb, resources=None, km=None):
        print("================TigerPreprocessorV2=============preprocess============================================")
        super(TigerPreprocessorV2, self).preprocess(nb, resources, km)

    def preprocess_cell(self, cell, resources, index):
        print("================TigerPreprocessorV2=============preprocess_cell=========================================")
        super(TigerPreprocessorV2, self).preprocess_cell(cell, resources, index)


print("=====================tiger_preprocessor_v2.py=========================")
