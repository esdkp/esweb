#!/bin/bash

PYTHON=python3
VIRTUALENV=virtualenv-3.4
VENV=venv

BREW_PACKAGES="tmux postgresql"
APT_PACKAGES="tmux postgresql"

if [ ! -d $VENV ] ; then
  echo "Virtual Environment not found, creating it now at $(pwd)/${VENV}"
  $VIRTUALENV -p $PYTHON --no-site-packages $VENV
fi

echo "Sourcing VENV"
source $VENV/bin/activate

echo "Updating pip via requirements.txt"
pip install -r requirements.txt

echo "Checking for other needed programs for development"
platform=$(uname)
if [[ "$platform" == "Darwin" ]] ; then
  if ! which brew ; then
    echo "Please install homebrew so I can install dependencies"
    exit 1
  else
    brew install ${BREW_PACKAGES}
  fi
elif [[ "$platform" == "Linux" ]] ; then
  if which apt-get ; then
    sudo apt-get install ${APT_PACKAGES}
  else
    echo "Unhandled linux platform - you'll need to set things up yourself"
    exit 1
  fi
else
  echo "Unhandled platform $platform - you'll need to manually set things up"
  exit 1
fi
