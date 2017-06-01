#!/usr/bin/env bash
python3 TFMSTGCA/automata.py > /dev/null &
nosetests --with-coverage