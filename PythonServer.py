
# import socket programming library 
import socket 
#import binascii
#import sys
from twilio.rest import Client
import time
  
# import thread module 
from _thread import *
import threading 
  
print_lock = threading.Lock() 
filepath = "output.txt"
output = open(filepath, "w+")
  
# thread fuction 
def threaded(c): 
    while True: 
  	
        # data received from client
        data = c.recv(1024).decode("utf-8")
        data = float(data)
        print(data)

        if not data:
            print('Bye')
	
            # lock released on exit
            print_lock.release()
            break
	
     	# send text if threshold is reached
        if data > 85:
            print("Threshold reached! Alerting user...")

            # Your Account SID from twilio.com/console
            account_sid = 'AC420a1f9d56eba4c4ab39c5aea9979036'
            # Your Auth Token from twilio.com/console
            auth_token  = 'fecdb7c4c03fcc752739a4089651fafb'

            client = Client(account_sid, auth_token)

            message = client.messages \
                            .create(
                                body="Your hottub is primed and ready!",
                                from_='+18604312955',
                                to='+14134265884'
                            )

            print(message.sid)
            print_lock.release()
            break

    # connection closed 
    c.close() 
  
  
def Main(): 
    host = "" 
  
    # reverse a port on your computer 
    # in our case it is 12345 but it 
    # can be anything 
    port = 3389
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port)) 
    print("socket binded to post", port) 
  
    # put the socket into listening mode 
    s.listen(5) 
    print("socket is listening") 
  
    # a forever loop until client wants to exit 
    while True: 
  
        # establish connection with client 
        c, addr = s.accept() 
  
        # lock acquired by client 
        print_lock.acquire() 
        print('Connected to :', addr[0], ':', addr[1]) 
  
        # Start a new thread and return its identifier 
        start_new_thread(threaded, (c,)) 
    s.close() 
  
  
if __name__ == '__main__': 
    Main() 
