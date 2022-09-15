#!/usr/bin/python3
# prints all the stuff in the sniffed packet, including destination ip address etc

import socket, sys, time 
from struct import pack

def send(ip, port, sock, values):
    print(values[0]) 
    args = ["<Q11B12H"] # A longlong timestamp, 11 Bytes, the rest are 16bit shorts
    args.append(values[0])
    for i in values[1]:   # append the Bytes
        args.append(i)

    args.append(values[2])
    args.append(values[3])
    for i in values[4]:   # append the shorts
        args.append(i)
    sock.sendto(pack(*args), (ip, port))

def main(message=0):

    port = 5432     #arbitrary port
#    ip = "172.17.0.1"
    ip = "127.0.0.1"
    freq = 1
    period = (1 / freq)

    print("UDP target IP: {}".format(ip))
    print("UDP target port: {}".format(port))
    print("message: {}".format(message))
    clock = 0
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    time.sleep(1)
    while True:
        timestamp = 123456
        Bytes = [10, 11, 12, 13, 14, 15, 35, 34, 33, 32, 31]
        shorts = range(100, 110)
        val1, val2 = (1111, 2222)
        payload = [timestamp, Bytes, val1, val2, shorts]
        send(ip, port, sock, payload)
        time.sleep(3)

if __name__ == "__main__":
    main(*sys.argv[1:])
