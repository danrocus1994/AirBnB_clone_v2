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
sudo ln -s /data/web_static/releases/test /data/web_static/current
