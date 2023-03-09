FROM ubuntu:latest

ARG HUGO=hugo_0.111.2_linux-amd64
ARG HUGO_VER=v0.111.2

# general setup
RUN apt-get update && \
    apt-get -y install vim wget sudo git 

RUN wget https://github.com/gohugoio/hugo/releases/download/$HUGO_VER/$HUGO.deb && apt-get -y install ./$HUGO.deb

# User account
ENV USER=ubuntu

# Setup default user
RUN useradd --create-home -s /bin/bash -m $USER && echo "$USER:ubuntu" | chpasswd && adduser $USER sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

WORKDIR /home/$USER
USER $USER

