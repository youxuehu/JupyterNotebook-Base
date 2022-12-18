# -*- coding:utf-8 -*-
from JupyterNotebookBase.utils.log_utils import get_logger
from JupyterNotebookBase.utils import json_utils

log = get_logger(__name__)


def post_save_hook(os_path, model, contents_manager):
    logger = contents_manager.log
    # logger.info("os_path at %s" % os_path)
    msg = json_utils.dumps_with_datetime(model, True)
    logger.info("model at\n %s" % msg)
