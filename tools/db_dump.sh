#!/bin/sh
path=$(dirname $(readlink -f $0))
mysqldump -u root -p pa > "$path/../database/pa.sql"
