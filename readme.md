docker build . -t tiger.com/1:20211211

docker run --name jupyternotebookbase -p 8888:8888 -it -d 8cb40e57ad30 /bin/bash "nohup /JupyterNotebook-Base/install.sh >> /root/install.log 2 >&1 $ echo $! > /root/install.pid"

docker run --name jupyternotebookbase -p 9999:8888 -it -d 455748f0ecf7 /bin/bash /JupyterNotebook-Base/install.sh