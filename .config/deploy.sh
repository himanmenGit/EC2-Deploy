#!/usr/bin/env bash
export DJANGO_SETTINGS_MODULE=config.settings.dev
sudo rm -rf /etc/nginx/sites-enabled/*
sudo cp -f /srv/ec2-deploy2/.config/nginx-app.conf /etc/nginx/sites-available/nginx-app.conf
sudo ln -sf /etc/nginx/sites-available/nginx-app.conf /etc/nginx/sites-enabled/nginx-app.conf
sudo cp -f /srv/ec2-deploy2/.config/uwsgi.service /etc/systemd/system/uwsgi.service

# collectstatic을 위한 과정
cd /srv/ec2-deploy2/app
# ubuntu유저로 collectstatic명령어를 실행 (deploy스크립트가 root권한으로 실행되므로)
/bin/bash -c \
'/home/ubuntu/.pyenv/versions/fc-ec2-deploy2/bin/python \
/srv/ec2-deploy2/app/manage.py collectstatic --noinput' ubuntu

sudo systemctl enable uwsgi
sudo systemctl daemon-reload
sudo systemctl restart uwsgi nginx