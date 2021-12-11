# -*- coding:utf-8 -*-
from JupyterNotebookBase.jupyter_extensions import current_dir
from JupyterNotebookBase import MY_DEFAULT_STATIC_FILES_PATH, MY_DEFAULT_TEMPLATE_PATH_LIST
from notebook import DEFAULT_STATIC_FILES_PATH, DEFAULT_TEMPLATE_PATH_LIST
import os
import shutil

jupyter_notebook_config = os.path.join(current_dir, "jupyter_notebook_config.py")  # noqa
jupyter_nbconvert_config = os.path.join(current_dir, "jupyter_nbconvert_config.py")  # noqa


def main():
    shutil.copy(
        jupyter_notebook_config, os.path.join(os.getenv("JUPYTER_CONFIG_HOME"), "jupyter_notebook_config.py")
    )  # noqa
    shutil.copy(
        jupyter_nbconvert_config, os.path.join(os.getenv("JUPYTER_CONFIG_HOME"), "jupyter_nbconvert_config.py")
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


# def copy(src, target):
#     static_list_file = os.listdir(src)
#     for file in static_list_file:
#         shutil.copy(os.path.join(src, file), os.path.join(target, file))
