import socket

MAX_SIZE_BYTES = 65535
hostname = "127.0.0.1"
cskt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    cskt.connect((hostname, 3000))
    msg = input("enter msg: ")
    data = msg.encode("ascii")
    cskt.send(data)
    mss = cskt.recv(MAX_SIZE_BYTES)
    mss.decode("ascii")
    print(mss)

