#!/usr/bin/env python3
import socket                   # Import socket module
from cryptography.fernet import Fernet

port = 50000                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = "localhost"     # Get local machine name

key = Fernet.generate_key()

with open('mykey.key', 'wb') as mykey:
    mykey.write(key)

with open('manav.txt', 'rb') as original_file:
      original = original_file.read()

enc = key.encrypt(original)

with open ('enc_manav.txt', 'wb') as encrypted_file:
   encrypted_file.write(enc)

s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print ('Server listening....')

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print ('Got connection from', addr)
    data = conn.recv(1024)
    print('Server received', repr(data))

    filename='enc_manav.txt'
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
       conn.send(l)
       print('Sent ',repr(l))
       l = f.read(1024)
    f.close()

    print('Done sending')
    conn.send('Thank you for connecting'.encode())
    conn.close()