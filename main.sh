#!/usr/bin/env bash

# Bitcoin Wallet
# ------------------------------------------------------------------------------
# josemariasosa ☠️


PYTHON_FOLDER='./app'
PYTHON_EXECUTER=$PYTHON_FOLDER'/venv/bin/python'
PYTHON_FILE=$PYTHON_FOLDER'/main.py'

source .env
$PYTHON_EXECUTER $PYTHON_FILE