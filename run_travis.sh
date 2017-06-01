#!/usr/bin/env bash
python automata.py > /dev/null &
nosetests --with-coverage