#!/bin/bash

apt update
apt-get install -y build-essential
apt-get install -y vim
apt-get install -y tmux
apt-get install -y make
apt-get install -y cmake
apt-get install -y git
git clone https://github.com/cboswel/MARTe-demos.git
