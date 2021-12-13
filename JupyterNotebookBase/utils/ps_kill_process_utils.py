# -*- coding:utf-8 -*-
import os
import codecs
import psutil


def kill_process(pid_path, log):
    if os.path.isfile(pid_path):
        with codecs.open(pid_path, "r", encoding="utf-8") as fin:
            pid = fin.read()
        if pid:
            process_list = psutil.process_iter()
            for proc in process_list:
                if int(pid.rstrip()) == int(proc.pid):
                    p = psutil.Process(proc.pid)
                    if not "SYSTEM" in p.name():  # noqa
                        # 杀不死啊
                        proc.kill()
                        log.info("Kill process at path: %s" % pid_path)
