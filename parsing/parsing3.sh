#!/bin/bash

export marte_mds_path=Trees/
./scriptingTest.sh &>/dev/null &
./Main.sh -l RealTimeLoader -f 3-UDP.cfg -s Run
pkill "UDPSmall.py"
