import socket

MAX_SIZE_BYTES = 65535
cskt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = input("Enter sentence:")
data = message.encode("ascii")
cskt.sendto(data, ("127.0.0.1", 3000))
data, address = cskt.recvfrom(MAX_SIZE_BYTES)
message = data.decode("ascii")
print(f"Response from server {message!r}")
