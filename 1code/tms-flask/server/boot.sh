#! /bin/bash


source /home/ubuntu/projects/graduation-design/1code/tms-flask/venv/bin/activate

source ./../../config.conf

export TMS_CONFIG=$config_name

gunicorn -w 4 -b $gunicorn_tms_ip:$gunicorn_tms_port -t 160 manage:app --log-level DEBUG
