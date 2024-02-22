"""
Client for Local Network Chat

This script creates a simple chat client that connects to a server over a local network and allows the user to send and receive messages.

Usage:
    - Run this script on each machine where you want to have a chat client.
    - Change the SERVER_IP variable to the IP address of the machine running the server.
    - Clients can communicate with each other through the central server.

Requirements:
    - Python 3.x

"""

import socket
import threading

def receive_messages():
    """
    Receive and display messages from the server.

    """
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            message = data.decode('utf-8')
            print(message)
        except:
            break

def send_message():
    """
    Send messages to the server.

    """
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))

# Change this to the IP address of the machine running the server
SERVER_IP = 'localhost'
SERVER_PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

send_thread = threading.Thread(target=send_message)
send_thread.start()
