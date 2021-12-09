# -*- coding:utf-8 -*-
from notebook.base.handlers import IPythonHandler  # noqa
from concurrent.futures import ThreadPoolExecutor  # noqa
import json
from tornado import gen, concurrent  # noqa
from notebook.utils import url_path_join  # noqa
from JupyterNotebookBase.jupyter_extensions.user_definition_config import get_user_definition_config


class UserDefinitionConfigHandler(IPythonHandler):  # noqa
    def get_request_param(self, key, require=True):
        if self.request.headers["Content-Type"] == "application/json":
            args = json.loads(self.request.body)
            val = args.get(key)
        else:
            val = self.get_argument(key)
        if require and val is None:
            raise Exception("missing required param %s" % key)

        return val

    def get(self):
        data = get_user_definition_config()
        self.log.info("data type %s" % type(data))
        self.write(json.dumps(data))


def load_jupyter_server_extension(nb_app):
    web_app = nb_app.web_app
    host_pattern = ".*$"
    route_pattern = url_path_join(web_app.settings["base_url"], "/user/definition/config")
    web_app.add_handlers(host_pattern, [(route_pattern, UserDefinitionConfigHandler)])
