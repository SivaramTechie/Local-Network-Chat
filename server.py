"""
Server for Local Network Chat

This script creates a simple chat server that allows multiple clients to connect over a local network and chat with each other.

Usage:
    - Run this script on a machine that will act as the server.
    - Clients connect to the server's IP address and port to participate in the chat.

Requirements:
    - Python 3.x

"""

import socket
import threading

def handle_client(client_socket, address):
    """
    Handle communication with a client.

    Parameters:
        - client_socket (socket): The socket object for the client.
        - address (tuple): The client's address (IP, port).

    """
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        message = data.decode('utf-8')
        print(f"Received from {address}: {message}")
        broadcast(message, client_socket)

    print(f"Connection from {address} closed.")
    client_sockets.remove(client_socket)
    client_socket.close()

def broadcast(message, sender_socket):
    """
    Broadcast a message to all connected clients.

    Parameters:
        - message (str): The message to broadcast.
        - sender_socket (socket): The socket of the client sending the message.

    """
    for client in client_sockets:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                client_sockets.remove(client)

HOST = '0.0.0.0'
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"Server listening on {HOST}:{PORT}")

client_sockets = []

while True:
    client_socket, address = server_socket.accept()
    print(f"Accepted connection from {address}")
    
    client_sockets.append(client_socket)

    client_handler = threading.Thread(target=handle_client, args=(client_socket, address))
    client_handler.start()
