# TFMSTGCA

Final work of the masters on Simulation of tumor growths with cellular automata.

[![Build Status](https://travis-ci.org/MULCIA/TFMSTGCA.svg?branch=master)](https://travis-ci.org/MULCIA/TFMSTGCA)
[![Coverage Status](https://coveralls.io/repos/github/MULCIA/TFMSTGCA/badge.svg?branch=master)](https://coveralls.io/github/MULCIA/TFMSTGCA?branch=master)
[![Code Health](https://landscape.io/github/MULCIA/TFMSTGCA/master/landscape.svg?style=flat)](https://landscape.io/github/MULCIA/TFMSTGCA/master)

## Introduction

This project pretend to reproduce "Analysis of behaviour transitions in tumour growth using a cellular automaton simulation" paper from José Santos and Ángel Monteagudo (2014).

In this paper, the authors used computational biology as an approach for analysing dynamics of tumor growth at celular level. In detail, they applied cellular automata for modelling behaivor of cells using cancer cell hallmark.

## Dependencies

* [NumPy](http://www.numpy.org/). 
* [Matplotlib](https://matplotlib.org/).

## Installation

To develop this project, and for running it, Python3 is required. But, first of all, `requirements.txt` must be installed.

`$ pip3 install -r requirements.txt`

## Running

For running it, type:

`$ python3 automata.py`