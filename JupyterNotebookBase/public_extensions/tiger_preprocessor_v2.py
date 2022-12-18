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
        self.executed_cells = []

    def preprocess(self, nb, resources=None, km=None):  # noqa
        print("param_file_path: %s" % self.param_file_path)
        os.environ["CURRENT_IPYNB_PARAM_PATH"] = self.param_file_path
        print("================TigerPreprocessorV2=============preprocess========================================")
        return super(TigerPreprocessorV2, self).preprocess(nb, resources, km)

    def preprocess_cell(self, cell, resources, index, **kwargs):  # noqa
        global error_raise
        # print(
        #    "================TigerPreprocessorV2=============preprocess_cell=================================== %s"
        #    % cell
        # )  # noqa
        # print("TigerPreprocessorV2")
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
                    print()
                    print(out["text"], file=sys.stdout, flush=True)

            # self._store_variable(cell, index)
            return cell, resources
        except CellExecutionError as e:
            error_raise = True
            return cell, resources
        finally:
            # notebook 执行时，cell 执行的 print 日志需要出书到sls
            # 2个方案:
            # 1：cell 执行完将日志 stdout
            # 2：每执行一个 cell 就输出一个 html
            self._output_html(index)

    def _store_variable(self, cell, index):
        new_cell = self.execute_cell(cell=new_code_cell(source="%who"), cell_index=index, store_history=True)
        print()
        # print(new_cell.outputs[0]["text"])
        print()
        import sys

        for out in new_cell.outputs:
            if "text" in out:
                # 写入文件
                print()
                print(out["text"], file=sys.stdout, flush=True)
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
                    print()
                    # print(msg)
                except Exception:  # noqa
                    pass
        self.nb["cells"][index] = cell

    def _output_html(self, index):
        # self._method_1(index)
        self._method_2(index)

    def _method_1(self, index):
        """
        方法一
        :param index:
        :return:
        """
        try:
            import nbformat

            nbformat.write(self.nb, "/tmp/nbconvert.ipynb")
            import os
            import time

            self.log.info("Execute cell index at %d is finished" % (index + 1))
            os.system(
                "jupyter-nbconvert --to html /tmp/nbconvert.ipynb --output /Users/youxuehu/PycharmProjects/JupyterNotebook-Base/tmp/%s"  # noqa
                % str(time.time())
            )
        except Exception as e:
            pass

    def _method_2(self, index):
        """
        方法2
        :param index:
        :return:
        """
        import copy
        from JupyterNotebookBase.public_extensions.tiger_executors import TigerHTMLExporter
        import codecs

        # 步骤1：过滤未执行的 cell，记录已执行的 cell
        copy_nb = copy.deepcopy(self.nb)
        copy_resources = copy.deepcopy(self.resources)
        self.executed_cells.append(self.nb["cells"][index])
        copy_nb["cells"] = self.executed_cells

        # 步骤2：将已执行测 cell 调用 jinjia2 模版引擎转换成 html 文本
        html = TigerHTMLExporter()
        output, resource = html.from_notebook_node(copy_nb, resources=copy_resources)
        if index == 0:
            print("resource: %s" % resource)
        with codecs.open("/Users/youxuehu/PycharmProjects/JupyterNotebook-Base/tmp/%d.html" % index, "w", encoding="utf-8") as f:  # noqa
            f.write(output)
