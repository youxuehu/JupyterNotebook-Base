# -*- coding:utf-8 -*-
from nbconvert.preprocessors.execute import ExecutePreprocessor  # noqa
from nbformat.v4.nbbase import new_code_cell  # noqa
from nbconvert.preprocessors import CellExecutionError  # noqa
import os

error_raise = False


class TigerPreprocessorV2(ExecutePreprocessor):
    def __init__(self, param_file_path, **kw):
        print("=====================tiger_preprocessor_v2.py=========================")
        super(TigerPreprocessorV2, self).__init__(**kw)
        self.param_file_path = param_file_path

    def preprocess(self, nb, resources=None, km=None):  # noqa
        print("param_file_path: %s" % self.param_file_path)
        os.environ["CURRENT_IPYNB_PARAM_PATH"] = self.param_file_path
        print("================TigerPreprocessorV2=============preprocess========================================")
        return super(TigerPreprocessorV2, self).preprocess(nb, resources, km)

    def preprocess_cell(self, cell, resources, index, **kwargs):  # noqa
        global error_raise
        print(
            "================TigerPreprocessorV2=============preprocess_cell=================================== %s"
            % cell
        )  # noqa
        try:
            # cell, resources = super(TigerPreprocessorV2, self).preprocess_cell(cell, resources, index)
            from nbclient.client import NotebookClient, run_sync
            self._check_assign_resources(resources)
            # Because nbclient is an async library, we need to wrap the parent async call to generate a syncronous version.
            cell = run_sync(NotebookClient.async_execute_cell)(self, cell, index, store_history=self.store_history)

            import sys
            for out in cell.outputs:
                if "text" in out:
                    # 写入文件
                    print(out["text"], sys.stdout, flush=True)

            new_cell = self.execute_cell(cell=new_code_cell(source="%who"), cell_index=index, store_history=True)
            print()
            print(new_cell.outputs[0]["text"])
            print()
            import sys
            for out in new_cell.outputs:
                if "text" in out:
                    # 写入文件
                    print(out["text"], sys.stdout, flush=True)
            if new_cell.outputs[0]["text"]:
                for v in new_cell.outputs[0]["text"].split("\t"):
                    try:
                        msg = self.execute_cell(
                            cell=new_code_cell(source="%store {}".format(v.strip())),
                            cell_index=index,
                            store_history=True,
                        ).outputs[0][
                            "text"
                        ]  # noqa
                        print(msg)
                    except Exception:  # noqa
                        pass
            self.nb["cells"][index] = cell
            return cell, resources
        except CellExecutionError as e:
            error_raise = True
            return cell, resources
