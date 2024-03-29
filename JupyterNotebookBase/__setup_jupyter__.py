# -*- coding:utf-8 -*-
from JupyterNotebookBase.jupyter_extensions import current_dir
from JupyterNotebookBase.ipython_extensions import current_dir as ipy_dir
from JupyterNotebookBase import MY_DEFAULT_STATIC_FILES_PATH, MY_DEFAULT_TEMPLATE_PATH_LIST
from notebook import DEFAULT_STATIC_FILES_PATH, DEFAULT_TEMPLATE_PATH_LIST
import os
import shutil
import sys

jupyter_notebook_config = os.path.join(current_dir, "jupyter_notebook_config.py")  # noqa
jupyter_nbconvert_config = os.path.join(current_dir, "jupyter_nbconvert_config.py")  # noqa
ipython_config = os.path.join(ipy_dir, "ipython_config.py")


def __replace_kernel_zmq_channels_api():

    src_url = "utils.url_path_join(that.kernel_url, 'channels')"
    target_url = "utils.url_path_join(that.kernel_url, 'channels_tiger')"

    kernel_js = os.path.join(DEFAULT_STATIC_FILES_PATH, "services/kernels/kernel.js")
    if os.path.exists(kernel_js):
        with open(kernel_js, "+r", encoding="utf-8") as f:
            content = f.read()
            content = content.replace(src_url, target_url)
            f.seek(0, 0)
            f.write(content)
            f.truncate()


def main():
    os.environ["JUPYTER_CONFIG_HOME"] = "%s/.jupyter" % os.getenv("HOME")
    os.environ["IPYTHON_PROFILE_PATH"] = "%s/.ipython" % os.getenv("HOME")
    if sys.platform == "linux":
        os.environ["JUPYTER_CONFIG_HOME"] = "/root/.jupyter"
    if not os.path.exists(os.environ["JUPYTER_CONFIG_HOME"]):
        os.makedirs(os.environ["JUPYTER_CONFIG_HOME"])
    if not os.path.exists(os.environ["IPYTHON_PROFILE_PATH"]):
        os.makedirs(os.environ["IPYTHON_PROFILE_PATH"])
    shutil.copy(
        jupyter_notebook_config, os.path.join(os.getenv("JUPYTER_CONFIG_HOME"), "jupyter_notebook_config.py")
    )  # noqa
    shutil.copy(
        jupyter_nbconvert_config, os.path.join(os.getenv("JUPYTER_CONFIG_HOME"), "jupyter_nbconvert_config.py")
    )  # noqa
    shutil.copy(
        ipython_config, os.path.join(os.getenv("IPYTHON_PROFILE_PATH"), "ipython_config.py")
    )  # noqa
    # copy(MY_DEFAULT_STATIC_FILES_PATH, DEFAULT_STATIC_FILES_PATH)
    # copy(MY_DEFAULT_TEMPLATE_PATH_LIST, DEFAULT_TEMPLATE_PATH_LIST)
    if os.path.exists(os.path.join(DEFAULT_STATIC_FILES_PATH, "my_js")):
        os.system("rm -rf %s" % os.path.join(DEFAULT_STATIC_FILES_PATH, "my_js"))
    os.system(
        "cp -R %s %s"
        % (os.path.join(MY_DEFAULT_STATIC_FILES_PATH, "my_js"), os.path.join(DEFAULT_STATIC_FILES_PATH, "my_js"))
    )  # noqa
    if os.path.exists(os.path.join(DEFAULT_TEMPLATE_PATH_LIST[1], "my_template")):
        os.system("rm -rf %s" % os.path.join(DEFAULT_TEMPLATE_PATH_LIST[1], "my_template"))
    os.system(
        "cp -R %s %s"
        % (
            os.path.join(MY_DEFAULT_TEMPLATE_PATH_LIST, "my_template"),
            os.path.join(DEFAULT_TEMPLATE_PATH_LIST[1], "my_template"),
        )
    )  # noqa

    # 替换 js
    # todo 废弃
    # __replace_kernel_zmq_channels_api()


# def copy(src, target):
#     static_list_file = os.listdir(src)
#     for file in static_list_file:
#         shutil.copy(os.path.join(src, file), os.path.join(target, file))
