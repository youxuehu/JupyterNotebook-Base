# -*- coding:utf-8 -*-
import os
import codecs
import sys

lines = [
    "c.InteractiveShellApp.log_level = 20",
    "c.InteractiveShellApp.exec_lines = [\"%matplotlib inline\"]",
    "c.InteractiveShellApp.extensions = [\"JupyterNotebookBase.ipython_extensions.load_ipython_extension\"]",
]
if sys.platform == "linux":
    os.environ["IPYTHON_PROFILE_PATH"] = "/root/.ipython/profile_default"
elif sys.platform == "darwin":
    os.environ["IPYTHON_PROFILE_PATH"] = "/Users/youxuehu/.ipython/profile_default"
with codecs.open(os.path.join(os.getenv("IPYTHON_PROFILE_PATH"), "ipython_config.py"), "w") as fout:
    fout.write("\n".join(lines))
