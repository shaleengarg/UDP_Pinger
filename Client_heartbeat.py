#!/usr/bin/python

from socket import *
from datetime import datetime

Array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def main():
    print "Original work by Shaleen Garg, 201401069"
    serverName = '127.0.0.1'  ##localhost
    serverPort = 12000 ## port number
    counter = 0

    # message = raw_input('send something') ## send something to client and input

    while counter < 10:    
        
        mySocket = socket(AF_INET, SOCK_DGRAM)  ## udp socket
        mySocket.settimeout(1.0)
        tstart = datetime.now()
        message = 'ping ' + str(counter+1) + ' ' + str(tstart) ##counter number
        counter += 1
        
        try:
            mySocket.sendto(message, (serverName, serverPort))
            message_return, address = mySocket.recvfrom(1024)
            tend = datetime.now()

        except timeout:
            Array[counter-1] = -1
            print 'Request timeout!'
            mySocket.close()

        else:
            uptime = tend - tstart
            Array[counter-1] = (tend - tstart)
            print 'Server Response: ' + message_return + ' RTT: ' + str(uptime) + ' secs'

    Time_sort()
    mySocket.close()
    pass


def Time_sort():
    flag = 0
    count = 0
    a = 0
    for i in range(0,10):
        if Array[i] != -1:
            a += 1
            if flag == 0:
                Max_time = Array[i]
                Min_time = Array[i]
                Avg_time = Array[i]
                flag = 1
            if Array[i] > Max_time:
                Max_time = Array[i]
            elif Array[i] < Min_time:
                Min_time = Array[i]
            Avg_time += Array[i]

        else:
            count += 1
    print ""
    print "##########################################"
    print 'Max Ping Time ', Max_time, 'seconds'
    print 'Min Ping Time ', Min_time, 'seconds'
    print 'Avg Ping Time', Avg_time/a, 'seconds'
    print 'Packet Loss Rate', count*10, '%'
    print "##########################################"

if __name__ == '__main__':
    main()