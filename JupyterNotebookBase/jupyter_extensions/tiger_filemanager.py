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


class TigerFileManager(LargeFileManager):
    name = Unicode("", config=True, help="""name """)

    port = Integer(TORNADO_PORT, config=True, help="Port of the server to be killed. Default %s" % TORNADO_PORT)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ConfigConstants.name = self.name
        ConfigConstants.port = self.port

    def get(self, path, content=True, type=None, format=None):  # noqa
        self.log.info("Welcome to TigerFileManager.get.")
        self.log.info("Welcome to TigerFileManager.get > path at %s" % path)
        self.log.info("Welcome to TigerFileManager.get > content at %s" % content)
        self.log.info("Welcome to TigerFileManager.get > type at %s" % type)
        self.log.info("Welcome to TigerFileManager.get > format at %s" % format)
        return super(TigerFileManager, self).get(path, content, type, format)

    def save(self, model, path=""):
        self.log.info("Welcome to TigerFileManager.save.")
        return super(TigerFileManager, self).save(model, path)
