#! /bin/bash

tms_pids=`sudo lsof -i:5000 | grep 'gunicorn' | awk '{print $2}'`
oauth2_pids=`sudo lsof -i:5001 | grep 'gunicorn' | awk '{print $2}'`

python3 monitor.py $1 $tms_pids $oauth2_pids

# usage: $bash monitor.sh 60