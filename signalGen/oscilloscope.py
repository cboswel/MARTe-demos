#!/bin/python3

import matplotlib.pyplot as plt
import subprocess

output = subprocess.getoutput('head -n -1 wave.csv | tail -n -100')
Y = output.splitlines()

plt.ion()
graph = plt.plot(Y)[0]
plt.axis([0, 100, -10, 10])
plt.ylabel('amplitude')

while True:

    output = subprocess.getoutput('head -n -1 wave.csv | tail -n -100')
    Y = output.splitlines()
    graph.set_ydata(Y)
    plt.draw()
    plt.pause(0.01)
