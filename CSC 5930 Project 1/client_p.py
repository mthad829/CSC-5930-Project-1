import socket                   # Import socket module
from cryptography.fernet import Fernet  

s = socket.socket()             # Create a socket object
host = socket.gethostname()     #Ip address that the TCPServer  is there
port = 50000                    # Reserve a port for your service every new transfer wants a new port or you must wait.

key = "VlD8h2tEiJkQpKKnDNKnu8ya2fpIBMOo5oc7JKNasvk="
k = Fernet(key)

s.connect((host, port))
s.send("Hello Server".encode())



with open('received_file', 'wb') as f:
    print('file opened')
    while True:
        print('receiving data...')
        # decrypts the data in the file using the key
        data = k.decrypt(s.recv(1024))
        print('data=%s', (data))
        if not data:
            break
        # write data to a file
        f.write(data)

f.close()
print('Successfully get the file')
s.close()
print('connection closed')