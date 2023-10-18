#!/bin/bash

# 打开终端并执行指令
gnome-terminal --tab --title="Terminal 1" --command="bash -c 'cd OnlineJudge-master; python3 manage.py runserver 0.0.0.0:8000; read -p PressEnter'"
gnome-terminal --tab --title="Terminal 2" --command="bash -c 'cd OnlineJudge-master; python3 manage.py rundramatiq --processes 2 --threads 2; read -p PressEnter'"
gnome-terminal --tab --title="Terminal 3" --command="bash -c 'cd OnlineJudgeFE-master; npm run dev; read -p PressEnter'"

