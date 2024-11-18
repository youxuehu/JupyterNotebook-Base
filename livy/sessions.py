# -*- coding:utf-8 -*-
import requests

DEFAULT_HEADERS = {
    "accept": "application/json"
}
params = {
    "kind": "spark"
}
r = requests.post("http://127.0.0.1:8998/sessions", json=params, headers=DEFAULT_HEADERS)
print(r.content.decode())
