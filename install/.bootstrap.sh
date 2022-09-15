#!/bin/bash

apt update
apt-get install -y build-essential libcap-dev
apt-get install -y vim
apt-get install -y tmux
apt-get install -y make
apt-get install -y cmake
apt-get install -y git
apt-get install -y python3
git clone https://github.com/cboswel/MARTe-demos.git
