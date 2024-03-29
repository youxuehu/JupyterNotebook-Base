# -*- coding:utf-8 -*-
import json
import requests  # noqa
from requests.compat import urljoin  # noqa
from nbformat.v4 import output_from_msg  # noqa
from JupyterNotebookBase.utils.log_utils import get_logger

log = get_logger(__name__)


def get_notebook_kernel_id(nb_file_name):
    try:
        from notebook.notebookapp import list_running_servers  # noqa

    except ImportError:
        import warnings
        from IPython.utils.shimmodule import ShimWarning  # noqa

        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=ShimWarning)
            from IPython.html.notebookapp import list_running_servers  # noqa
    from requests.compat import urljoin

    servers = list_running_servers()
    log.info("servers: %s" % servers)
    try:
        for server in servers:
            log.info("server: %s" % server)
            params = {"token": server.get("token", "")}
            log.info("params: %s" % params)
            log.info("urljoin: %s" % urljoin(server["url"], "api/sessions"))
            response = requests.get(urljoin(server["url"], "api/sessions"), params=params)
            log.info("response: %s" % response)
            for kernel in json.loads(response.text):
                log.info("kernel: %s" % kernel)
                if nb_file_name in kernel["path"]:
                    log.info("n_path: %s" % kernel["path"])
                    kernel_id = kernel["kernel"]["id"]
                    log.info("kernel_id: %s" % kernel_id)
                    return kernel_id
    except Exception as e:
        print("%s" % e)


def run_code(kernel_client, lines):
    kernel_client.start_channels()
    kernel_client.wait_for_ready(30)
    cmd = "\n".join(lines)
    msg_id = kernel_client.execute(cmd)
    return msg_id


def run_code_with_kernel(kernel_client, lines):
    status, res = False, None
    try:
        kernel_client.start_channels()
        kernel_client.wait_for_ready(30)
        cmd = "\n".join(lines)
        msg_id = kernel_client.execute(cmd)
        status, res = get_result(kernel_client, msg_id)
        print("status: %s, res: %s" % (status, res))
    except Exception as e:
        print("%s" % e)
    finally:
        if kernel_client:
            kernel_client.stop_channels()
    return status, res


def get_result(kernel_client, msg_id):
    outs = []
    status, res = False, None
    while True:
        try:
            import asyncio

            loop = asyncio.get_event_loop()
            msg = loop.run_until_complete(kernel_client.iopub_channel.get_msg(timeout=10))
            print("msg: %s" % msg)
            if msg["parent_header"].get("msg_id") != msg_id:
                continue
            msg_type = msg["msg_type"]
            content = msg["content"]
            if msg_type == "status":
                if content["execution_state"] == "idle":
                    break
            elif msg_type == "clear_output":
                pass
            elif msg_type["execute_input"] or msg_type.startswith("comm"):
                continue
            else:
                outs.append(output_from_msg(msg))
        except Exception:  # noqa
            pass

    if outs and "data" in outs[-1]:
        if "text/html" in outs[-1]["data"]:
            status, res = True, outs[-1]["data"]["text/html"]
        elif "text/plain" in outs[-1]["data"]:
            status, res = True, outs[-1]["data"]["text/plain"]
    if outs and ("output_type" in outs[-1]) and (outs[-1]["output_type"] == "error"):  # noqa
        print("outs error %s" % outs)
        status, res = False, outs[-1]["evalue"]  # noqa
    return status, res
