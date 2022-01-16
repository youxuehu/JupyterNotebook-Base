# -*- coding:utf-8 -*-
import subprocess

process = subprocess.Popen("kubectl get deploy -n kubeflow | awk 'NR > 1 {print $1}'", stdout=subprocess.PIPE, shell=True)
output = process.communicate()[0].decode("utf-8")
for out in output.split("\n"):
    print(out)
    import os
    os.system("kubectl delete deployment %s -n kubeflow" % out)
