#!/bin/sh
path=$(dirname $(readlink -f $0))
mysql -u root -p pa < "$path/../database/pa.sql"
