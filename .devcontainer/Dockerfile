FROM ubuntu:22.04

ARG TARGETPLATFORM

RUN apt-get update && \
    apt-get -y install vim wget sudo git 

RUN case ${TARGETPLATFORM} in \
         "linux/amd64")  HUGO=hugo_0.111.2_linux-amd64 ;; \
         "linux/arm64")  HUGO=hugo_0.111.2_linux-arm64 ;; \
    esac \
    && HUGO_VER=v0.111.2 \
    &&  wget https://github.com/gohugoio/hugo/releases/download/${HUGO_VER}/${HUGO}.deb && apt-get -y install ./${HUGO}.deb

# User account
ENV USER=ubuntu

# Setup default user
RUN useradd --create-home -s /bin/bash -m $USER && echo "$USER:ubuntu" | chpasswd && adduser $USER sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

WORKDIR /home/$USER
USER $USER

