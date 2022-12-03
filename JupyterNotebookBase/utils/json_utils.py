# -*- coding:utf-8 -*-
import json


def dumps(data, pretty=False):
    if pretty:
        return json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
    return json.dumps(data)