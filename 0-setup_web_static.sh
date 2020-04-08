#!/usr/bin/env bash
# Setup Web servers with Nginx Airbnb Deploy
sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/{shared,releases/test}
sudo tee /data/web_static/releases/test/index.html <<EOF
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
sudo ln -s /data/web_static/releases/test /data/web_static/current
sudo chown ubuntu:ubuntu /data/
sudo tee /etc/nginx/sites-available/default > /dev/null <<EOF                                    
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name localhost;    
    location /hbnb_static {
        alias /data/web_static/current/;
	try_files \$uri \$uri/ =404;
    }
}
EOF
/etc/init.d/nginx restart
