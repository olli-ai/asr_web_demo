FROM ubuntu:20.04

MAINTAINER Hung <hung@olli-ai.com>

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Ho_Chi_Minh
RUN apt-get update && apt-get install -y --no-install-recommends locales git apt-utils && \
  apt-get -y install --no-install-recommends python3 python3-pip python3-dev build-essential && \
  apt -y install make cmake gcc g++ ffmpeg && \
  apt -y install libsndfile1-dev && \
  pip3 install --upgrade pip && \
  locale-gen en_US.UTF-8  && \
  rm -rf /var/lib/apt/lists/*

COPY  .  /src/
# RUN pip3 install torch
RUN pip3 install -r /src/requirements.txt && \
	cd /src && make 

RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

#ENV MODEL_BASE_PATH=/models

# serving port (flask)
EXPOSE 5000

WORKDIR /src

# run main.py
ENTRYPOINT 	["python3", "main.py"]
