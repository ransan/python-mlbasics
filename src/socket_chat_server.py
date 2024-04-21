import socket

MAX_SIZE_BYTES = 65535
hostname = "127.0.0.1"
sskt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sskt.bind((hostname, 3000))
while True:
    data, ip= sskt.recvfrom(MAX_SIZE_BYTES)
    msg = data.decode("ascii")
    print(msg)
    reply = input("enter reply: ")
    reply_msg= reply.encode("ascii")
    sskt.sendto(reply_msg, ip)