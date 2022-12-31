# -*- coding:utf-8 -*-
import psutil  # noqa
import os
from pexpect import replwrap  # noqa
from JupyterNotebookBase.utils.log_utils import get_logger

log = get_logger(__name__)


def kill_9(name="nginx"):

    pids = replwrap.bash().run_command(
        "ps -ef | grep %s | grep -v grep | awk '{print $2}'" % name, timeout=None
    )
    log.warn("************** 杀死 pid ***********")
    log.warn("************** pid 查询：***********")
    pids = pids.split("\r\n")
    pids = list(filter(lambda pid: pid != "" or pid is not None, pids))
    log.warn(pids)
    for pid in pids:
        if pid.rstrip() == "":
            continue
        os.system("kill -9 %s" % pid)
        log.warn("Kill pid %s" % pid)


if __name__ == "__main__":
    kill_9(name="nginx")