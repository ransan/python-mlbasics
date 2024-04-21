import socket

MAX_SIZE_BYTES=65535
skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port=3000
hostname="127.0.0.1"
skt.bind((hostname, port))
while True:
    data, clientAddress = skt.recvfrom(MAX_SIZE_BYTES)
    message = data.decode('ascii')
    uppercaseMessage = message.upper()
    print(f"The client address {clientAddress!r}, data {uppercaseMessage!r}")
    data = uppercaseMessage.encode("ascii")
    skt.sendto(data, clientAddress)