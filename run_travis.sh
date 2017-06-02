#!/usr/bin/env bash
python3 main.py > /dev/null &
nosetests --with-coverage