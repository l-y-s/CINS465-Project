#!/bin/bash
ifconfig
python /code/manage.py runserver 0.0.0.0:8000
/code/start-channelserver.sh
/code/start-channelworker.sh

