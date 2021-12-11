FROM ubuntu:18.04

RUN mkdir /JupyterNotebook-Base
ADD . /JupyterNotebook-Base/
ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"
RUN apt-get update

RUN apt-get install -y wget && rm -rf /var/lib/apt/lists/*
# RUN apt-get install -y vim
# RUN apt-get install -y tree

RUN mkdir /root/.conda \
    && bash /JupyterNotebook-Base/Miniconda3-4.3.27-Linux-x86_64.sh -b
RUN pip list
RUN conda  info
RUN pip install setuptools_scm
RUN pip install notebook -i https://pypi.tuna.tsinghua.edu.cn/simple
# RUN pip install jupyterlab -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install pandas -i https://pypi.tuna.tsinghua.edu.cn/simple