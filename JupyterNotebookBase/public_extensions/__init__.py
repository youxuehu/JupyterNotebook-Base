# -*- coding:utf-8 -*-
import os


current_dir = os.path.dirname(__file__)
print(current_dir)
monitor_base_path = "/tmp/monitor"
monitor_log_path = "/root/monitor_event_%s.log"
monitor_pid_path = "/root/monitor_event_%s.pid"
