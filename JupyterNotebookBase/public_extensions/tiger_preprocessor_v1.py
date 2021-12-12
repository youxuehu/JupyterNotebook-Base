# -*- coding:utf-8 -*-
from nbconvert.preprocessors.execute import ExecutePreprocessor  # noqa
from nbconvert.preprocessors import CellExecutionError  # noqa
error_raise = False


class TigerPreprocessorV1(ExecutePreprocessor):
    def __init__(self, param_file_path, **kw):
        print("=====================tiger_preprocessor.py=========================")
        super(TigerPreprocessorV1, self).__init__(**kw)
        self.param_file_path = param_file_path

    def preprocess(self, nb, resources=None, km=None):  # noqa
        print("param_file_path: %s" % self.param_file_path)
        print("================TigerPreprocessor=============preprocess============================================")
        return super(TigerPreprocessorV1, self).preprocess(nb, resources, km)

    def preprocess_cell(self, cell, resources, index, **kwargs):  # noqa
        global error_raise
        print("================TigerPreprocessor=============preprocess_cell=========================================%s" % cell)  # noqa
        try:
            return super(TigerPreprocessorV1, self).preprocess_cell(cell, resources, index)
        except CellExecutionError as e:
            error_raise = True
            return cell, resources
