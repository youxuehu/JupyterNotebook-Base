# -*- coding:utf-8 -*-
from JupyterNotebookBase.constants.config_constants import ConfigConstants
from JupyterNotebookBase.utils.log_utils import get_logger

log = get_logger(__name__)


def get_user_definition_config():
    data = dict()
    name = ConfigConstants.name
    port = ConfigConstants.port
    log.info("user definition config name is %s" % name)
    log.info("user definition config port is %s" % port)
    data["name"] = ConfigConstants.name
    data["port"] = ConfigConstants.port
    return data
