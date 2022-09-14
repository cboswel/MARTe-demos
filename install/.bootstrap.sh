#!/bin/bash

apt update
apt-get install -y build-essential libcap-dev
apt-get install -y vim
apt-get install -y tmux
apt-get install -y make
apt-get install -y cmake
apt-get install -y git
apt-get install -y autotools-dev
apt-get install -y libtool
apt-get install -y automake
apt-get install -y autogen
apt-get install -y libpcap-dev
git clone https://github.com/appneta/tcpreplay.git
cd /tcpreplay
pwd
#./autogen
#./configure --disable-local-libopts
#make
#make install
#cd /
#git clone https://github.com/cboswel/MARTe-demos.git
