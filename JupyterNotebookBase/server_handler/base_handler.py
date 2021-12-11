# -*- coding:utf-8 -*-
from notebook.base.handlers import IPythonHandler  # noqa
import json


class BaseHandler(IPythonHandler):
    def get_request_param(self, key, require=True):
        self.log.info("self.request.headers: %s" % self.request.headers)
        if "Content-Type" in self.request.headers.keys() and self.request.headers["Content-Type"] == "application/json":
            self.log.info("self.request.body: %s" % str(self.request.body, encoding="utf-8"))
            args = json.loads(str(self.request.body, encoding="utf-8"))
            val = args.get(key)
        else:
            val = self.get_argument(key)
        if require and val is None:
            raise Exception("missing required param %s" % key)

        return val
