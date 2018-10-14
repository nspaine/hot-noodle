# Import socket module 
import socket 
import serial

serial_port = '/dev/ttyACM0';
baud_rate = 9600; #In arduino, Serial.begin(baud_rate)

ser = serial.Serial(serial_port, baud_rate)  
  
def Main(): 
    # local host IP
    host = #put your IP address here!
  
    # Define the port on which you want to connect 
    port = #put your port number here!
  
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
  
    # connect to server on local computer 
    s.connect((host,port)) 
  
    while True: 
        line = ser.readline()
        line = line.decode("utf-8") #ser.readline returns a binary, convert to string
        print(line);   

        # message sent to server 
        s.send(line.encode('ascii')) 
  
if __name__ == '__main__': 
    Main()
