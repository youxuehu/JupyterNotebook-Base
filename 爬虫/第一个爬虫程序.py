# -*- coding:utf-8 -*-
import requests

r = requests.get("https://v1.kwaicdn.com/upic/2022/11/05/20/BMjAyMjExMDUyMDI5MTNfMTk4MDUwNDM2N184ODA0NTEwNDc0M18xXzM=_hd15_Bbc65b3add84dad72e2ea2937497b2ed3.mp4?pkey=AAXLDaTrNpALUtVKUOYplgGY10TSu5YE_OjVi5hg0IUSHLirm2BiHLwm7063wjQvScTnYhtLlV6wV3U4B2WUrngaV3rrKWay2Tze7-wcLX0jQZwzYl-Qu3P002ZOiCDdTj4&tag=1-1670508141-unknown-0-6mykptra0j-c7c47716a6482309&clientCacheKey=3xvijpuw4d54rj9_hd15.mp4&di=JAiDQAgjGgCg54ZbQBzJIg==&bp=10004&tt=hd15&ss=vp")  # noqa
with open("1.mp4", "wb") as f:
    f.write(r.content)
