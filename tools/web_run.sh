#!/bin/sh
path=$(dirname $(readlink -f $0))
echo $(date) > "$path/../log/web.log"
nohup python "$path/../web.py" >> "$path/../log/web.log" 2>&1 &
