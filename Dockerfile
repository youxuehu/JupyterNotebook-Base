FROM ubuntu:18.04

RUN mkdir /JupyterNotebook-Base
ADD . /JupyterNotebook-Base/
ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"
RUN apt-get update

RUN apt-get install -y wget && rm -rf /var/lib/apt/lists/*
# RUN apt-get install -y vim
# RUN apt-get install -y tree

RUN cd /tmp
RUN wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-latest-Linux-x86_64.sh
RUN mkdir /root/.conda
RUN bash Miniconda3-latest-Linux-x86_64.sh -b
RUN pip list
RUN conda info
RUN pip install notebook -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
RUN pip install pandas -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
RUN pip install nbconvert -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
RUN pip install odps -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
RUN pip install oss2 -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
RUN mkdir -p /Users/youxuehu/PycharmProjects/JupyterNotebook-Base
RUN mkdir -p /root/.jupyter
RUN mkdir -p /root/.ipython/profile_default
RUN touch /root/install.log
RUN touch /root/install.pid
ENV JUPYTER_CONFIG_HOME /root/.jupyter
ENV IPYTHON_PROFILE_PATH /root/.ipython/profile_default
ENV PYTHONPATH /root/miniconda3/lib/python3.6/site-packages/JupyterNotebookBase/public_extensions