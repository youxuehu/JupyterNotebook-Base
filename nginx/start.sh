cp ./* $OPENRESTY_ETC/
python kill.py
nginx -c /usr/local/etc/openresty/notebook.conf



