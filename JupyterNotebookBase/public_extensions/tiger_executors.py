# -*- coding:utf-8 -*-
import sys
from nbconvert import HTMLExporter
from nbconvert.postprocessors import PostProcessorBase
from JupyterNotebookBase.utils.common_utils import is_new_notebook

if is_new_notebook():
    from JupyterNotebookBase.public_extensions.tiger_preprocessor_v2 import (TigerPreprocessorV2 as TigerPreprocessor, error_raise) # noqa
else:
    from JupyterNotebookBase.public_extensions.tiger_preprocessor import (TigerPreprocessor, error_raise) # noqa


class TigerHTMLExporter(HTMLExporter):
    def __init__(self, config=None, **kw):
        super(TigerHTMLExporter, self).__init__(config, **kw)


class TigerPostprocessor(PostProcessorBase):
    def postprocess(self, input):
        if error_raise:
            sys.exit(1)
