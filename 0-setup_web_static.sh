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
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown ubuntu:ubuntu -R /data
tee /etc/nginx/sites-available/default > /dev/null <<EOF
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name localhost;
  
    location /hbnb_static {
        alias /data/web_static/current/;
    }
}
EOF
service nginx restart
