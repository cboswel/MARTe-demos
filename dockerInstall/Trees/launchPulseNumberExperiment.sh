export marte_mds_path=$(pwd)

g++ -g -Wall -I. -I/usr/local/mdsplus/include/ -L/usr/local/mdsplus/lib64 -lMdsObjectsCppShr PulseNumberExperiment.cpp -o PulseNumberExperiment.ex


./PulseNumberExperiment.ex
