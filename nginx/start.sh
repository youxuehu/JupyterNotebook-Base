set -x
cp ./* $OPENRESTY_ETC/
ps -ef|grep nginx
python kill.py
nginx -c /usr/local/etc/openresty/image.conf
ps -ef|grep nginx
set +x


