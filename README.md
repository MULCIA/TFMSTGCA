# TFMSTGCA

Final work of the masters on Simulation of tumor growths with cellular automata.

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/73e679fe51764a57a0cdf3d634e41a80)](https://www.codacy.com/app/serrodcal/TFMSTGCA?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=MULCIA/TFMSTGCA&amp;utm_campaign=Badge_Grade)
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

![Grid example. Yellow is healty and green is cancer.](./readme_images/grid_example.png)

## Running on Docker

If you prefer not to install anything in your environment, you can use Docker.

This project has a folder which it has some scripts to help you with docker in case you do not know docker.

Previously, you have to give execution permission to `.sh` files in `script_docker` folder: `$ chmod r+x script_docker/*`

### Build image

You can use `$ ./script_docker/build.sh` or type `docker build -t serrodcal/tfm .`.

### Run container

You can use `$ ./script_docker/run.sh` or type `docker run --name tfm -d serrodcal/tfm:latest tail -f /dev/null`.

### Get terminal

You can use `$ ./script_docker/terminal.sh` or type `docker exec -it tfm bash`.

### Start container

You can use `$ ./script_docker/start.sh` or type `docker start tfm`.

### Stop container

You can use `./script_docker/stop.sh` or type `docker stop tfm`.

### Clean everything

You can use `$ ./script_docker/clean.sh` or:

```
$ docker rm $(docker ps -a | grep tfm)
$ docker rmi $(docker images | grep tfm)
$ docker rmi $(docker images | grep ubuntu)
```

## Travis in local environment

Run `$ docker run --name tfm -v ~/Repositories/TFMSTGCA:/home/TFMSTGCA -ti quay.io/travisci/travis-python /bin/bash`, then
to run inside docker container following commands:

* `$ cd /home/TFMSTGCA`
* `$ pip3 install -r requirements.txt`
* `$ ./run_travis.sh`
