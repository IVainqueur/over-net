import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific network interface and port
s.bind(("", 12345))

def execCommand(command):
    print("Executing command: ", command)
    return {'success': True, 'message': ''}

while True:
    # Receive data from the socket
    data, addr = s.recvfrom(1024)

    # decode the data
    data = data.decode()

    # Print the received message
    print("Received message: ", data)

    # Check if the message is a command
    if data.startswith('command:'):
        # Execute the command
        result = execCommand(data[8:])

        # Send the result back to the client
        s.sendto(str(result).encode(), addr)

# Close the socket
s.close()

