# -*- coding:utf-8 -*
import psutil  # noqa
import codecs
import os
from JupyterNotebookBase.utils.log_utils import get_logger

log = get_logger(__name__)

notebook_pid_path = "/Users/youxuehu/PycharmProjects/JupyterNotebook-Base/jupyter.pid"


def main():
    if not os.path.isfile(notebook_pid_path):
        return
    with codecs.open(
        notebook_pid_path, mode="r", encoding="utf-8"
    ) as fin:
        pid = fin.read()
    if not pid:
        return
    process_list = psutil.process_iter()
    for proc in process_list:
        if pid != proc.pid:
            continue
        p = psutil.Process(proc.pid)
        if not "SYSTEM" in p.name():  # noqa
            proc.kill()
            log.warn("Kill jupyter notebook process kill, pid is %s" % pid)


if __name__ == "__main__":
    main()
