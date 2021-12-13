# -*- coding:utf-8 -*-
import pyinotify  # noqa
import asyncio
from JupyterNotebookBase.utils.log_utils import get_logger
import argparse
import os

log = get_logger(__name__)

monitor_path = None


def handle_callback(notifier):  # noqa
    if not monitor_path:
        return
    if not os.path.isdir(monitor_path):  # noqa
        return
    file_list = os.listdir(monitor_path)  # noqa
    file_list = list(filter(lambda file: os.path.isfile(os.path.join(monitor_path, file)), file_list))  # noqa
    print(file_list)


def main():
    parser = argparse.ArgumentParser(description="this is a description")
    parser.add_argument("--monitor_path", help="monitor path")
    args = parser.parse_args()
    wm = pyinotify.WatchManager()
    loop = asyncio.get_event_loop()
    notifier = pyinotify.AsyncioNotifier(wm, loop, callback=handle_callback)
    log.info("Monitor path at %s" % args.monitor_path)
    multi_event = pyinotify.IN_CREATE | pyinotify.IN_MODIFY
    global monitor_path
    monitor_path = args.monitor_path
    wm.add_watch(args.monitor_path, multi_event)
    loop.run_forever()
    notifier.stop()


if __name__ == "__main__":
    main()
