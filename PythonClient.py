# Import socket module 
import socket 
import serial

serial_port = '/dev/ttyACM0';
baud_rate = 9600; #In arduino, Serial.begin(baud_rate)

ser = serial.Serial(serial_port, baud_rate)  
  
def Main(): 
    # local host IP '127.0.0.1' 
    host = '35.229.99.112'
  
    # Define the port on which you want to connect 
    port = 3389
  
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
  
    # connect to server on local computer 
    s.connect((host,port)) 
  
    while True: 
        line = ser.readline()
        line = line.decode("utf-8") #ser.readline returns a binary, convert to string
        print(line);   

        # message sent to server 
        s.send(line.encode('ascii')) 

        # messaga received from server 
        #data = s.recv(1024) 

        # print the received message 
        # here it would be a reverse of sent message 
        #print('Received from the server :',str(data.decode('ascii'))) 
  
    # close the connection 
    # s.close() 
  
if __name__ == '__main__': 
    Main()