import socket

target_host = "0.0.0.0"
target_port = 9998

#creating the socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connecting the client
client.connect((target_host,target_port))

# sending data through the socket
client.send(b"hello")

# receive some data with 4096 bits allowed
response = client.recv(4096)

print(response.decode())
client.close()