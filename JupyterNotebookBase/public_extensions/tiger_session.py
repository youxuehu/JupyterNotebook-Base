# -*- coding:utf-8 -*-
from notebook.services.sessions.sessionmanager import SessionManager  # noqa
from tornado import gen  # noqa
import copy
import os
import re
import json
import codecs
from JupyterNotebookBase.utils.log_utils import get_logger
from notebook.utils import maybe_future

log = get_logger(__name__)


class HubSessionManager(SessionManager):
    def __init__(self, **kw):
        super(HubSessionManager, self).__init__(**kw)

    @gen.coroutine
    def start_kernel_for_session(self, session_id, path, name, type, kernel_name):
        env = copy.copy(os.environ)
        pattern = re.compile(r"notebook_(\d+).ipynb")
        m = pattern.match(name)
        if m is not None:
            node_id = m.group([0])
            os.system("osscmd -H xxx -i xxx -k xxx ")
            try:
                with open("/ossfs/.%s_param.conf" % node_id, "r", encoding="UTF-8") as f:
                    content = f.read()
                    params = json.loads(content)
            except Exception as e:  # noqa
                params = dict()
        else:
            params = dict()
        lines = params
        # 启动监听服务
        name_split = name.split(".")
        _start_monitor_service(name_split[0])
        kernel_path = self.contents_manager.get_kernel_path(path=path)
        kernel_id = yield gen.maybe_future(
            self.kernel_manager.start_kernel(path=kernel_path, kernel_name=kernel_name, env=env, inject_lines=lines)
        )
        raise gen.Return(kernel_id)


class HubSessionManagerV2(SessionManager):
    def __init__(self, **kw):
        super(HubSessionManagerV2, self).__init__(**kw)

    @gen.coroutine
    def start_kernel_for_session(self, session_id, path, name, type, kernel_name):
        env = copy.copy(os.environ)
        pattern = re.compile(r"notebook_(\d+).ipynb")
        m = pattern.match(name)
        params = {}
        if m is not None:
            node_id = m.group([0])
            param_file_path = "/ossfs/.%s_param.conf" % node_id
            if os.path.exists(param_file_path):
                with codecs.open(param_file_path, "r", encoding="UTF-8") as f:
                    content = f.read()
                params = json.loads(content)
        lines = ['name="zhangsan"']
        # 启动监听服务
        self.log.info("start kernel for session session_id: %s" % session_id)
        self.log.info("start kernel for session path: %s" % path)
        self.log.info("start kernel for session name: %s" % name)
        self.log.info("start kernel for session type: %s" % type)
        self.log.info("start kernel for session kernel_name: %s" % kernel_name)
        path_split = path.split("/")
        file_name = path_split[len(path_split) - 1].split(".")[0]
        _start_monitor_service(file_name)
        kernel_path = self.contents_manager.get_kernel_path(path=path)
        from notebook.utils import maybe_future  # noqa

        kernel_id = yield maybe_future(
            self.kernel_manager.start_kernel(path=kernel_path, kernel_name=kernel_name, env=env, inject_lines=lines)
        )
        raise gen.Return(kernel_id)

    @gen.coroutine
    def delete_session(self, session_id):
        """
        关闭 session 的时候
        :param session_id:
        :return:
        """
        session = yield maybe_future(self.get_session(session_id=session_id))
        self.log.info("session_id: %s" % session_id)
        self.log.info("session: %s" % session)
        super(HubSessionManagerV2, self).delete_session(session_id)
        path = session["path"]
        self.log.info("path: %s" % path)
        path_split = path.split("/")
        file_name = path_split[len(path_split) - 1].split(".")[0]
        self.log.info("file_name: %s" % file_name)
        from JupyterNotebookBase.public_extensions import monitor_base_path, monitor_pid_path

        monitor_pid_path = monitor_pid_path % file_name
        from JupyterNotebookBase.utils.ps_kill_process_utils import kill_process

        kill_process(monitor_pid_path, self.log)
        monitor_path = os.path.join(monitor_base_path, file_name)
        if os.path.isdir(monitor_path):
            os.system("rm -rf %s" % monitor_path)


def _start_monitor_service(name):

    from JupyterNotebookBase.public_extensions import monitor_base_path, monitor_log_path, monitor_pid_path

    monitor_log_path = monitor_log_path % name
    monitor_pid_path = monitor_pid_path % name
    monitor_path = os.path.join(monitor_base_path, name)
    if os.path.isdir(monitor_path):
        log.info("Monitor service has been start up, monitor path at %s" % monitor_path)
        return
    os.makedirs(monitor_path)

    os.system(
        "nohup jupyternotebookbase_monitor_event --monitor_path=%s >> %s 2>&1 & echo $! > %s"
        % (monitor_path, monitor_log_path, monitor_pid_path)
    )
    log.info(
        "Monitor service start up successful. log path at %s, pid path at %s, monitor path at %s"
        % (monitor_log_path, monitor_pid_path, monitor_path)
    )
