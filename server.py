
"""
def write_log(name, message):
"""
import hashlib
from socket import socket


def write_log(name, message):
    """
    write message to log file
    """
    # open log file
    with open('log.txt', 'a') as f:
        # write message to log file
        f.write(f'{name}: {message}\n')


def write_password(name, password):
    """
    write hashed password to password file
    """
    # open password file
    with open('password.txt', 'a') as f:
        # write hashed password to password file
        f.write(f'{name}: {hashlib.sha256(password.encode()).hexdigest()}\n')


def check_password(name, password):
    """
    check if password is correct
    """
    # open password file
    with open('password.txt', 'r') as f:
        # read all lines from password file
        lines = f.readlines()
        # check if name and password is correct
        for line in lines:
            if line.split(':')[0] == name and line.split(':')[1].strip() == hashlib.sha256(password.encode()).hexdigest():
                return True
        return False





def main():
    """
    start echo socket server
    on localhost:5000
    if port 5000 is busy then try 5001 and so on
    when new client connected ask him for his name and password
    if its is old client, he must enter his name and password
    password is stored like hash in file password.txt
    many messages can be sent to server
    input messages from client write in log file
    return to user his message
    """
    # create socket
    s = socket()
    # bind socket to localhost:5000
    port = 5000
    while True:
        try:
            s.bind(('localhost', port))
            break
        except OSError:
            port += 1
    # listen for connections
    s.listen()
    print(f'Listening on port {port}')
    # looped connection to client
    """Many messages can be sent to server"""
    while True:
        # accept connection from client
        conn, addr = s.accept()
        print(f'Connected to {addr}')
        # get name and password from client
        name = conn.recv(1024).decode()
        password = conn.recv(1024).decode()
        # check if name and password is correct
        if check_password(name, password):
            # send message to client
            conn.send('Welcome back!'.encode())
            # write Welcome back and name to log file
            write_log('Server', f'Welcome back! {name}')
            # looped connection to client
            while True:
                # get message from client
                message = conn.recv(1024).decode()
                # if message is exit then break
                # or if connection is lost then break
                if message == 'exit' or not message:
                    break
                if message == 'end':
                    return
                # write message to log file
                write_log(name, message)
                # send message to client
                conn.send(message.encode())
        else:
            # send message to client
            conn.send('Welcome!'.encode())
            # write hashed password to password file
            write_password(name, password)
            # write welcome and name to log file
            write_log(name, 'Welcome!')
        # close connection
        conn.close()


main()