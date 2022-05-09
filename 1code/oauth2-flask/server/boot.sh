#! /bin/bash

source /home/ubuntu/projects/graduation-design/1code/oauth2-flask/venv/bin/activate

source ./../../config.conf

export OAUTH2_CONFIG=$config_name

gunicorn -w 4 -b $gunicorn_oauth2_ip:$gunicorn_oauth2_port -t 160 manage:app --log-level DEBUG
