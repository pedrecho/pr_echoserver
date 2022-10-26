from socket import socket


def main():
    """
    create socket connection
    input ip and port
    if its incorrect use localhost:5000
    log in or register for name and password
    looped connection to server
    send message to server
    get message from server and output it
    """
    # create socket
    s = socket()
    # input ip and port
    ip = input('Enter ip: ')
    port = input('Enter port: ')
    # if ip or port is incorrect use localhost:5000
    if not ip or not port:
        ip = 'localhost'
        port = 5000
    # connect to server
    s.connect((ip, int(port)))
    # log in or register
    name = input('Enter your name: ')
    password = input('Enter your password: ')
    # send name and password to server
    s.send(name.encode())
    s.send(password.encode())
    # get message from server
    message = s.recv(1024).decode()
    print(message)
    # looped connection to server
    while True:
        # input message
        message = input('Enter message: ')
        # send message to server
        s.send(message.encode())
        # get message from server
        message = s.recv(1024).decode()
        print(message)

main()