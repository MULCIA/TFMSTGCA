FROM ubuntu:16.04

RUN apt-get update && \
    apt-get install -y python3 && \
    apt-get install -y python3-pip && \
    apt-get install -y git && \
    apt-get clean && \
    mkdir TFMSTGCA && \
    git clone https://github.com/MULCIA/TFMSTGCA.git /home/TFMSTGCA && \
    cd /home/TFMSTGCA && \
    pip3 install -r requirements.txt

WORKDIR /home/TFMSTGCA

RUN python3 -m unittest
