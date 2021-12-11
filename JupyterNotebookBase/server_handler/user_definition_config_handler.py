# -*- coding:utf-8 -*-
from JupyterNotebookBase.server_handler.base_handler import BaseHandler
import json
from notebook.utils import url_path_join  # noqa
from JupyterNotebookBase.jupyter_extensions.user_definition_config import get_user_definition_config
from JupyterNotebookBase import DEFAULT_STATIC_FILES_PATH, DEFAULT_TEMPLATE_PATH_LIST


class UserDefinitionConfigHandler(BaseHandler):  # noqa
    def get(self):
        data = get_user_definition_config()
        self.log.info("data type %s" % type(data))
        self.log.info("data json %s" % json.dumps(data, ensure_ascii=False, sort_keys=True))
        self.write(json.dumps(data, ensure_ascii=False, sort_keys=True))


def load_jupyter_server_extension(nb_app):
    settings = {"template_path": DEFAULT_TEMPLATE_PATH_LIST, "static_path": DEFAULT_STATIC_FILES_PATH}
    web_app = nb_app.web_app
    web_app.settings.update(settings)
    host_pattern = ".*$"
    route_pattern = url_path_join(web_app.settings["base_url"], "/user/definition/config")
    web_app.add_handlers(host_pattern, [(route_pattern, UserDefinitionConfigHandler)])
