#!/bin/bash

DBPATH=../db
DB=esweb
VENV_ACTIVATE=venv/bin/activate
TMUX_SESSION=esweb

if ! which tmux > /dev/null ; then
  echo "You need tmux, dummy."
  exit 1
fi

if tmux ls | grep ${TMUX_SESSION} ; then
  echo "tmux session found, attaching"
  tmux attach-session -t ${TMUX_SESSION}
  exit 0
fi

if [ ! -f ${VENV_ACTIVATE} ] ; then
  echo "VENV activation script not found at ${VENV_ACTIVATE}"
  echo "Ensure you're running this script from the root of the checkout"
  echo "and that you've set up the dev environment"
  exit 1
fi

if [ ! -d ${DBPATH} ] ; then
  echo "DB Directory (${DBPATH}) not found, creating"
  initdb $DBPATH
  createdb $DB
fi

echo "Loading virtual environment"
source ${VENV_ACTIVATE}

tmux start-server
tmux new-session -d -s ${TMUX_SESSION} -n postgres
tmux new-window -t ${TMUX_SESSION}:1 -n runserver
tmux new-window -t ${TMUX_SESSION}:2 -n shell

tmux send-keys -t ${TMUX_SESSION}:0 "postgres -h 127.0.0.1 -D ${DBPATH}" C-m
tmux send-keys -t ${TMUX_SESSION}:1 "source ${VENV_ACTIVATE} ; python manage.py runserver 0.0.0.0:8000" C-m
tmux send-keys -t ${TMUX_SESSION}:2 "source ${VENV_ACTIVATE}" C-m

tmux attach-session -t ${TMUX_SESSION}

