#!/bin/bash

export marte_mds_path=Trees/
./packetSender.sh &>/dev/null &
./Main.sh -l RealTimeLoader -f 3-UDP.cfg -s Run
pkill "UDPGenerator.py"
