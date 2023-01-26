import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific network interface and port
s.bind(("", 12345))

while True:
    # Receive data from the socket
    data, addr = s.recvfrom(1024)

    # Print the received message
    print("Received message: ", data.decode())

# Close the socket
s.close()
