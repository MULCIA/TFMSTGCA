FROM ubuntu:16.04

RUN apt-get update && \
    apt-get install -y python3 && \
    apt-get install -y python3-pip && \
    apt-get install -y git && \
    apt-get clean

WORKDIR /home

RUN git clone https://github.com/MULCIA/TFMSTGCA.git

WORKDIR /home/TFMSTGCA

RUN pip3 install -r requirements.txt

CMD ["python3", "-m", "unittest"]
