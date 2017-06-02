#!/usr/bin/env bash
python main.py > /dev/null &
nosetests --with-coverage