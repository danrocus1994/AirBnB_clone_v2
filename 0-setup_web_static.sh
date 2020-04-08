#!/usr/bin/env bash
# Setup Web servers with Nginx Airbnb Deploy
sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/{releases,shared,releases/test}
