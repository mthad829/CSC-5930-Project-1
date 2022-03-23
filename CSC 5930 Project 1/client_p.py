import socket                   # Import socket module
from cryptography.fernet import Fernet  

s = socket.socket()             # Create a socket object
host = "10.138.14.8"    #Ip address that the TCPServer  is there
port = 50000                    # Reserve a port for your service every new transfer wants a new port or you must wait.

key = "5HjdWe6TMIIbtsycc1l056f-a_SXwNtUsp0ujdoRN0I="
k = Fernet(key)

s.connect((host, port))
s.send("Hello Server".encode())

with open('received_file', 'wb') as f:
    print('file opened')
    while True:
        print('receiving data...')
        # decrypts the data in the file using the key
        data = s.recv(1024)
        print('data=%s', (data))
        if not data:
            break
        # write data to a file
        f.write(data)

with open('received_file', 'rb') as w:
    origData = w.read()
    dec_data = k.decrypt(origData)

with open('received_file_2', 'wb') as t:
    t.write(dec_data)

f.close()
print('Successfully get the file')
s.close()
print('connection closed')