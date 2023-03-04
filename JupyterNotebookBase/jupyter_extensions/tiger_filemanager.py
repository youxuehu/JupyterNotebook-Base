# -*- coding:utf-8 -*-
from notebook.services.contents.largefilemanager import LargeFileManager  # noqa
from traitlets import (  # noqa
    Any,
    Dict,
    Unicode,
    Integer,
    List,
    Bool,
    Bytes,
    Instance,  # noqa
    TraitError,
    Type,
    Float,
    observe,
    default,
    validate,  # noqa
)  # noqa
from JupyterNotebookBase.jupyter_extensions import TORNADO_PORT
from JupyterNotebookBase.constants.config_constants import ConfigConstants
from JupyterNotebookBase.utils import json_utils
import nbformat
import json
from nbformat.v4.rwbase import (
    rejoin_lines, strip_transient
)


class TigerFileManager(LargeFileManager):
    name = Unicode("", config=True, help="""name """)

    port = Integer(TORNADO_PORT, config=True, help="Port of the server to be killed. Default %s" % TORNADO_PORT)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ConfigConstants.name = self.name
        ConfigConstants.port = self.port

    def get(self, path, content=True, type=None, format=None):  # noqa
        # self.log.info("Welcome to TigerFileManager.get.")
        # self.log.info("Welcome to TigerFileManager.get > path at %s" % path)
        # self.log.info("Welcome to TigerFileManager.get > content at %s" % content)
        # self.log.info("Welcome to TigerFileManager.get > type at %s" % type)
        # self.log.info("Welcome to TigerFileManager.get > format at %s" % format)
        return super(TigerFileManager, self).get(path, content, type, format)

    def save(self, model, path=""):
        self.log.info("Welcome to TigerFileManager.save.")
        msg = json_utils.dumps_with_datetime(model, True)
        self.log.info("model at\n %s" % msg)
        return super(TigerFileManager, self).save(model, path)

    def _save_notebook(self, os_path, nb):
        self.log.info("_save_notebook................")
        # open(os_path, "w").write(json_utils.dumps_with_datetime(nb, True))
        # cell_dict = nb.get("cells")
        # for index, cell in enumerate(cell_dict):
        #     index_path = os_path + str(index)
        #     open(index_path, "w").write(json_utils.dumps_with_datetime(cell, True))
        #     nb.get("cells")[index] = index_path
        # open(os_path, "w").write(json_utils.dumps_with_datetime(nb, True))

    def _read_notebook(self, os_path, as_version=4):
        self.log.info("_read_notebook................")
        try:
            # nb = nbformat.reader.reads(open(os_path).read())
            nb = json.loads(open(os_path).read())
            if nb.get("cells"):
                for index, cell in enumerate(nb.get("cells")):
                    index_path = os_path + str(index)
                    nb.get("cells")[index] = json.loads(open(index_path, "r").read())
            nb = nbformat.from_dict(nb)
            nb = rejoin_lines(nb)
            nb = strip_transient(nb)
            # if nb.get("cells"):
            #     for index, cell in enumerate(nb.get("cells")):
            #         index_path = os_path + str(index)
            #         nb.get("cells")[index] = json.loads(open(index_path, "r").read())
            #     self.log.info("_read_notebook.......结束2.........")
            self.log.info("_read_notebook nb ===>")
            self.log.info(type(nb))
            self.log.info(json_utils.dumps(nb, True))
            return nb
        except Exception as ex:
            if ex:
                import traceback

                self.log.info(traceback.print_exc())
            with self.open(os_path, 'r', encoding='utf-8') as f:
                try:
                    nb = nbformat.read(f, as_version=as_version)
                    self.log.info("_read_notebook nb: " + str(nb))
                    return nb
                except Exception as e:
                    if e:
                        import traceback

                        self.log.info(traceback.print_exc())
