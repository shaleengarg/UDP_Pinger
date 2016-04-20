#!/usr/bin/python

# UDPPingerServer.py
# We will need the following module to generate randomized lost packets

import random
from socket import *
from datetime import datetime
import copy 
import sys 

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000)) ##localhost and port number 12000
serverSocket.settimeout(10.0)  ## it there is no communication in 10 sec, it will exit the server
last_number = 0
while True:
    
    # Generate random number in the range of 0 to 10
    rand = random.randint(0, 10)
    try:
        # Receive the client packet along with the address it is coming from
        message, address = serverSocket.recvfrom(1024)
        # Capitalize the message from the client
        Message = copy.deepcopy(message)
        time = str(datetime.now())
        Split_time = time.split()
        # print time
        # print message
       
        Split_message = Message.split()
        # print Split_message[1], last_number
        
        if (last_number+1) == int(Split_message[1]):
            # print "Recieved packet number " + str(last_number)
            last_number = int(Split_message[1])

        else:
            print "Lost packet number" + str(last_number)
            last_number = int(Split_message[1])

        if last_number == 10:  ## reset the value
            last_number = 0

        # print Split_message[3]  ##has the message time
        # print Split_time[1]   ## has the current time
        date_object_current = datetime.strptime(Split_time[1], '%H:%M:%S.%f')
        date_object_client = datetime.strptime(Split_message[3], '%H:%M:%S.%f')
        print "Time difference", (date_object_current- date_object_client), 'secs'
        # print date_object

        message = message.upper()# If rand is less is than 4, we consider the packet lost and do not respond
        if rand < 4:
            continue
            # Otherwise, the server responds
        serverSocket.sendto(message, address)
    
    except timeout:
        serverSocket.close()
        print "exiting, no activity after 10 secs"
        sys.exit()  