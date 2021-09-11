# -*- coding:utf-8 -*-
from nbconvert.preprocessors.execute import ExecutePreprocessor
from traitlets.traitlets import Unicode

error_raise = False


class TigerPreprocessorV2(ExecutePreprocessor):

    cell_source = Unicode(default_value="pwd", allow_none=False, help="cell source").tag(config=True)

    def preprocess(self, nb, resources=None, km=None):

        print("================TigerPreprocessorV2=============preprocess============================================")
        return super(TigerPreprocessorV2, self).preprocess(nb, resources, km)

    def preprocess_cell(self, cell, resources, index):
        print("================TigerPreprocessorV2=============preprocess_cell========================================")
        print("cell_source: %s" % self.cell_source)
        self.exec_cell_source(cell_source=self.cell_source, cell_index=index)
        print(cell.source)
        return super(TigerPreprocessorV2, self).preprocess_cell(cell, resources, index)

    def exec_cell_source(self, cell_source, cell_index):
        from nbformat.v4.nbbase import new_code_cell
        new_cell = new_code_cell(source=cell_source)
        output = self.execute_cell(cell=new_cell, cell_index=cell_index)
        print(output)


print("=====================tiger_preprocessor_v2.py=========================")
