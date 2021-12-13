set
cd /JupyterNotebook-Base
rm -rf build
rm -rf dist
rm -rf JupyterNotebookBase.egg-info
python setup.py bdist_wheel --universal
cd dist
pip uninstall -y JupyterNotebookBase
pip install JupyterNotebookBase-0.1.0-py2.py3-none-any.whl
cd ../
rm -rf build
rm -rf dist
rm -rf JupyterNotebookBase.egg-info
pip install notebook -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
pip install nbconvert -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
pip install psutil -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
pip install pyinotify -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
jupyternotebookbase_setup_jupyter
jupyternotebookbase_kill_notebook_process
# nohup jupyter notebook >> /Users/youxuehu/PycharmProjects/JupyterNotebook-Base/jupyter.log 2>&1 & echo $! > /Users/youxuehu/PycharmProjects/JupyterNotebook-Base/jupyter.pid
jupyter notebook