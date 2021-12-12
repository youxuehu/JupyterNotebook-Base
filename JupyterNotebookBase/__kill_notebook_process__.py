# -*- coding:utf-8 -*
import psutil  # noqa
import codecs
import os
from pexpect import replwrap  # noqa
from JupyterNotebookBase.utils.log_utils import get_logger

log = get_logger(__name__)

notebook_pid_path = "/Users/youxuehu/PycharmProjects/JupyterNotebook-Base/jupyter.pid"


def main():
    if not os.path.isfile(notebook_pid_path):
        return
    with codecs.open(notebook_pid_path, mode="r", encoding="utf-8") as fin:
        pid = fin.read()
    if not pid:
        return
    process_list = psutil.process_iter()
    for proc in process_list:
        if int(pid.rstrip()) == int(proc.pid):
            p = psutil.Process(proc.pid)
            if not "SYSTEM" in p.name():  # noqa
                # 杀不死啊
                proc.kill()
                log.warn("Kill jupyter notebook process, pid is %s" % pid)

    # kill_9()


def kill_9():

    pids = replwrap.bash().run_command(
        "ps -ef | grep \"jupyter-notebook\" | grep -v grep | awk '{print $2}'", timeout=None
    )
    pids = pids.split("\r\n")
    pids = list(filter(lambda pid: pid != "" or pid is not None, pids))
    for pid in pids:
        if pid.rstrip() == "":
            continue
        os.system("kill -9 %s" % pid)
        print("Kill pid %s" % pid)


if __name__ == "__main__":
    main()
