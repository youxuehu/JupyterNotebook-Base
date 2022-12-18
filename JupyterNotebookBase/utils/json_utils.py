# -*- coding:utf-8 -*-
import json
import datetime


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder.default(self, obj)


def dumps(data, pretty=False):
    if pretty:
        return json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
    return json.dumps(data)


def dumps_with_datetime(data, pretty=False):
    if pretty:
        return json.dumps(data, cls=DateEncoder, sort_keys=True, indent=4, separators=(',', ': '))
    return json.dumps(data)
