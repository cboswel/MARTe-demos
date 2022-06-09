#!/usr/bin/python3
# prints all the stuff in the sniffed packet, including destination ip address etc

import socket, sys, time 
from struct import pack

def send(ip, port, sock, values):
    print(values[0]) 
    args = ["200I"]#
    for i in values:
        args.append(i)
    sock.sendto(pack(*args), (ip, port))

def main(message=0):

    port = 5432     #arbitrary port
    ip = "127.0.0.1"
    freq = 1
    period = (1 / freq)

    print("UDP target IP: {}".format(ip))
    print("UDP target port: {}".format(port))
    print("message: {}".format(message))
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    time.sleep(1)
    while True:
        values = range(message, message+200)
        send(ip, port, sock, values)
        time.sleep(period)
        message = (message + 200)

if __name__ == "__main__":
    main(*sys.argv[1:])
