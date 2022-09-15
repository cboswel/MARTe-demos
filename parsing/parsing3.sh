#!/bin/bash

export marte_mds_path=Trees/
python3 UDPGenerator.py &>/dev/null &
./Main.sh -l RealTimeLoader -f 3-UDP.cfg -s Run
pkill "python3"
