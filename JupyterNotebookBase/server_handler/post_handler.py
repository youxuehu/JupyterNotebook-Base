# -*- coding:utf-8 -*-
import json
from notebook.utils import url_path_join  # noqa
from JupyterNotebookBase.jupyter_extensions.user_definition_config import get_user_definition_config
from JupyterNotebookBase import DEFAULT_STATIC_FILES_PATH, DEFAULT_TEMPLATE_PATH_LIST
from JupyterNotebookBase.server_handler.base_handler import BaseHandler


class PostHandler(BaseHandler):  # noqa
    def post(self):
        data = get_user_definition_config()
        self.log.info("data type %s" % type(data))
        self.log.info("data json %s" % json.dumps(data, ensure_ascii=False, sort_keys=True))
        success = self.get_request_param("success")
        city = self.get_request_param("city")
        data["success"] = success
        data["city"] = city
        # self.render("one.html", title="Data", data=data)
        self.finish(json.dumps(data, ensure_ascii=False, sort_keys=True))


def load_jupyter_server_extension(nb_app):
    settings = {"template_path": DEFAULT_TEMPLATE_PATH_LIST, "static_path": DEFAULT_STATIC_FILES_PATH}
    web_app = nb_app.web_app
    web_app.settings.update(settings)
    host_pattern = ".*$"
    route_pattern = url_path_join(web_app.settings["base_url"], "/post")
    web_app.add_handlers(host_pattern, [(route_pattern, PostHandler)])
