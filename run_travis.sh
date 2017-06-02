#!/usr/bin/env bash
python TFMSTGCA/automata.py > /dev/null &
nosetests --with-coverage