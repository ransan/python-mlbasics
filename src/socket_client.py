import socket

MAX_SIZE_BYTES = 65535
port=3000
cskt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
hosts=[]
while True:
    host = print("enter the host name:")
    hosts.append((host, port))
    message = input("Enter sentence:")
    data = message.encode("ascii")
    cskt.sendto((host, port))   
    data, address = cskt.recvfrom(MAX_SIZE_BYTES)
    message = data.decode("ascii")
    if(address in hosts):
        print(f"Response from server {message!r}")
        hosts.remove(address)
    else:
        print("unexpected host")


