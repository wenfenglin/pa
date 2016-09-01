#!/bin/sh
path=$(dirname $(readlink -f $0))
echo $(date) >> "$path/../log/crontab.log"
python "$path/../app.py" shows update all >> "$path/../log/crontab.log" 2>&1
