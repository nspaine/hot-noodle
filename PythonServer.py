
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
            account_sid = #insert account sid here!
            # Your Auth Token from twilio.com/console
            auth_token  = #insert auth token here!

            client = Client(account_sid, auth_token)

            message = client.messages \
                            .create(
                                body="Your hottub is primed and ready!",
                                from_= #insert twilio phone number here!,
                                to= #insert whatever phone number you want here!
                            )

            print(message.sid)
            print_lock.release()
            break

    # connection closed 
    c.close() 
  
  
def Main(): 
    host = "" 
 
    port = #insert port number here!
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
