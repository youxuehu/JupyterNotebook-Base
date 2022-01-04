# -*- coding:utf-8 -*-


def nbclient_execute(nb_file, timeout=None):
    import nbformat
    from nbclient import NotebookClient

    nb = nbformat.read(nb_file, as_version=4)

    client = NotebookClient(nb, timeout=timeout, kernel_name="python3")

    client.execute()

    nbformat.write(nb, "/tmp/$POD_NAME.ipynb")

    # import os
    # os.system(
    #     "jupyter-nbconvert --to html /tmp/$POD_NAME.ipynb --output /tmp/$POD_NAME.html"
    # )

    from nbconvert.exporters.html import HTMLExporter

    html = HTMLExporter()
    html.from_notebook_node(nb, resources=None)

