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
JupyterNotebookBase_setup_jupyter