#!/bin/bash

BASEDIR=$(pwd)
echo "building in $BASEDIR"

git clone https://github.com/aneto0/MARTe2-components.git
git clone https://github.com/aneto0/MARTe2.git

mv MARTe2 MARTe2-dev
export MARTe2_DIR=$BASEDIR/MARTe2-dev
export LD_LIBRARY_PATH=$MARTe2_DIR/Build/x86-linux/Core
export MARTe2_components_DIR=$BASEDIR/MARTe2-components

cd $MARTe2_DIR
make -f Makefile.linux

cd $MARTe2_components_DIR
make -f Makefile.linux

Build/x86-linux/GTest/MainGTest.ex


# MARTe install seems fine but MDSplus components arent getting installed because MDSplus install is botched. Dont forget to ./bootstrap then configure. Can generate buildroot with ../mdsplus/deploy/build.sh --os=ubuntu20 --release but I don't know how to install from there. 
