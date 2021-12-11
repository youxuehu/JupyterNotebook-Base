# -*- coding:utf-8 -*-
from JupyterNotebookBase.server_handler.base_handler import BaseHandler
import json
from notebook.utils import url_path_join  # noqa
from JupyterNotebookBase.jupyter_extensions.user_definition_config import get_user_definition_config
from tornado.web import RequestHandler


class TemplateHandler(BaseHandler):  # noqa
    def get(self):
        data = get_user_definition_config()
        self.log.info("data type %s" % type(data))
        self.log.info("data json %s" % json.dumps(data, ensure_ascii=False, sort_keys=True))
        success = self.get_request_param("success")
        city = self.get_request_param("city")
        data["success"] = success
        data["city"] = city

        self.log.info("RequestHandler._template_loaders %s" % RequestHandler._template_loaders)
        # self.render("my_template/template.html", title="Data", data=data)
        self.finish(json.dumps(data, ensure_ascii=False, sort_keys=True))


def load_jupyter_server_extension(nb_app):
    web_app = nb_app.web_app
    host_pattern = ".*$"
    route_pattern = url_path_join(web_app.settings["base_url"], "/template")
    web_app.add_handlers(host_pattern, [(route_pattern, TemplateHandler)])
