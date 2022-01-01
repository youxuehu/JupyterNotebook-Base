# -*- coding:utf-8 -*-
from JupyterNotebookBase.server_handler.base_handler import BaseHandler
import json
from notebook.utils import url_path_join  # noqa
from JupyterNotebookBase.utils import notebook_kernel_utils
from jupyter_client.blocking.client import BlockingKernelClient
import asyncio
from tornado import gen, concurrent, ioloop
from concurrent.futures import ThreadPoolExecutor


class ExecuteCodeHandler(BaseHandler):  # noqa
    def __init__(self, *args, **kwargs):
        max_cores = 4
        try:
            import psutil

            max_cores = psutil.cpu_count()
        except Exception as e:
            pass
        self.executor = ThreadPoolExecutor(max_cores)
        self.io_loop = ioloop.IOLoop.current()
        super(ExecuteCodeHandler, self).__init__(*args, **kwargs)

    @gen.coroutine
    def get(self):
        self.log.info("进入～")
        data = {"success": True}

        res = yield self.exec()
        data.update(res)
        self.finish(json.dumps(data, ensure_ascii=False, sort_keys=True))

    @concurrent.run_on_executor()
    def exec(self):
        code = self.get_argument("code")
        self.log.info("code： %s" % code)
        nb_file_name = self.get_argument("nb_file_name")
        self.log.info("nb_file_name： %s" % nb_file_name)
        kernel_id = notebook_kernel_utils.get_notebook_kernel_id(nb_file_name)
        self.log.info("kernel_id： %s" % kernel_id)
        # os.getenv("JUPYTER_RUNTIME_DIR")
        kc = BlockingKernelClient(
            connection_file="/Users/youxuehu/Library/Jupyter/runtime/kernel-%s.json" % kernel_id
        )  # noqa
        self.log.info("kc： %s" % kc)
        kc.load_connection_file()
        self.log.info("load_connection_file")
        asyncio.set_event_loop(asyncio.new_event_loop())
        msg_id = notebook_kernel_utils.run_code(kc, [code])
        self.log.info("msg_id： %s" % msg_id)
        res = {"msg_id": msg_id}
        return res


def load_jupyter_server_extension(nb_app):
    web_app = nb_app.web_app
    host_pattern = ".*$"
    route_pattern = url_path_join(web_app.settings["base_url"], "/exec/code")
    web_app.add_handlers(host_pattern, [(route_pattern, ExecuteCodeHandler)])
