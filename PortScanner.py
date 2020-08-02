import socket # for socket 
import sys  
  
try: 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(s)
    print("Socket successfully created")
except socket.error as err: 
    print ("socket creation failed with error %s" %(err) )
    sys.exit()

host_name = input("Enter the domain name")
port = int(input("Enter the port number"))
  
try: 
    host_ip = socket.gethostbyname(host_name) 
except: 
    print("there was an error resolving the host")
    sys.exit() 
  
# connecting to the server 
s.connect((host_ip, port)) 
  
print("The socket has been connected to  ip of {0} through the  port  {1} " .format(host_ip,port) )
