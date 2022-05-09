#! /bin/bash

sudo rm /etc/supervisor/conf.d/oauth2.conf
sudo rm /etc/supervisor/conf.d/tms.conf
sudo supervisorctl reload

sudo rm -rf oauth2-flask/venv/
sudo rm -rf tms-flask/venv/

sudo rm tms-flask/server/tms-dev.sqlite
sudo rm oauth2-flask/server/oauth2-dev.sqlite
