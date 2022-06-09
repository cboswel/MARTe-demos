#!/usr/bin/python3
# prints all the stuff in the sniffed packet, including destination ip address etc

import socket, sys, os, time, threading

def send(ip, port, sock, message):
    print(message) 
    sock.sendto(int(message).to_bytes(4, byteorder='little'), (ip, port)) 

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
        send(ip, port, sock, message)
        time.sleep(period)
        message = str(int(message) + 1)

if __name__ == "__main__":
    main(*sys.argv[1:])
