from socket import socket


def add_header(message):
    """
    l is len of mes
    if l >= 10000 l is 9999
    if l < 1000 add zeros to len l is 4
    """
    # get len of message
    l = len(message)
    # if len of message >= 10000 then len of message is 9999
    if l >= 10000:
        l = 9999
    # if len of message < 1000 then add zeros to len of message
    if l < 1000:
        l = '0' * (4 - len(str(l))) + str(l)
    # return len of message and message
    return str(l) + message


def read_header(message):
    """
    return mes without first four chars
    """
    # return message without first four chars
    return message[4:]


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
    s.send(add_header(name).encode())
    s.send(add_header(password).encode())
    # get message from server
    message = read_header(s.recv(1024).decode())
    print(message)
    # looped connection to server
    while True:
        # input message
        message = input('Enter message: ')
        # send message to server
        s.send(add_header(message).encode())
        # get message from server
        message = read_header(s.recv(1024).decode())
        print(message)

main()