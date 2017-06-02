#!/usr/bin/env bash
python3 TFMSTGCA/main.py > /dev/null &
nosetests --with-coverage