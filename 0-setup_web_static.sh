#!/usr/bin/env bash
# Setup Web servers with Nginx Airbnb Deploy
apt-get update
apt-get -y install nginx
mkdir -p /data/web_static/{shared,releases/test}
tee /data/web_static/releases/test/index.html <<EOF
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF
if [ -e /data/web_static/current ];then
    rm /data/web_static/current
fi
ln -sf /data/web_static/releases/test /data/web_static/current
chown ubuntu:ubuntu /data/
tee /etc/nginx/sites-available/default > /dev/null <<EOF
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name localhost;
  
    location /hbnb_static {
        alias /data/web_static/current/;
	try_files index.html =404;
    }
}
EOF
service nginx restart
