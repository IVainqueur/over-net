import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set the socket to allow broadcast
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Bind the socket to a specific network interface and port
s.bind(("", 12345))

# Create the message to be broadcast
message = "Hello, this is a broadcast message!"

# Send the broadcast message
s.sendto(message.encode(), ("255.255.255.255", 12345))

# Close the socket
s.close()
