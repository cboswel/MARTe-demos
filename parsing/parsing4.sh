#!/bin/bash

export marte_mds_path=Trees/
./packetSender.sh &>/dev/null &
./Main.sh -l RealTimeLoader -f 4-Types.cfg -s Run
pkill "UDPGenerator.py"

