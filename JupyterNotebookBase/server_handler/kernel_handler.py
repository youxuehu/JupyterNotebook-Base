# -*- coding:utf-8 -*-
from notebook.base.handlers import IPythonHandler  # noqa
import psutil  # noqa
from pexpect import replwrap  # noqa
import json
from tornado import gen, web
try:
    from jupyter_client.jsonutil import json_default
except ImportError:
    from jupyter_client.jsonutil import (
        date_default as json_default
    )
from notebook.utils import maybe_future
from JupyterNotebookBase.utils.json_utils import dumps


class KernelHandler(IPythonHandler):

    @web.authenticated
    @gen.coroutine
    def get(self, kernel_id):
        """
        http://localhost:9999/getKernelStatusById/93f49137-e3c7-481f-9117-e3b4108d1ba3
        :param kernel_id:
        :return:
        """
        self.log.info("kernel_id: %s" % kernel_id)
        km = self.kernel_manager
        model = yield maybe_future(km.kernel_model(kernel_id))
        kernel_pid = replwrap.bash().run_command(
            "ps -ef | grep \"kernel-%s\" | grep -v grep | awk '{print $2}'" % kernel_id, timeout=None
        )

        self.log.info("kernel_pid: %s" % kernel_pid)
        res = {
            "kernel_id": kernel_id,
            "status": model.get("execution_state"),
            "kernel_pid": kernel_pid.split("\r\n")[0]
        }
        self.log.info("res: %s" % dumps(res, True))
        self.finish(json.dumps(res, default=json_default))


_kernel_id_regex = r"(?P<kernel_id>\w+-\w+-\w+-\w+-\w+)"

default_handlers = [
    (r"/getKernelStatusById/%s" % _kernel_id_regex, KernelHandler),
]
