set -x
cp ./* $OPENRESTY_ETC/
ps -ef|grep nginx
nginx -s reload -c /usr/local/etc/openresty/image.conf
ps -ef|grep nginx
set +x


