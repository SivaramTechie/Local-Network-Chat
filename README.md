# Local Network Chat

A simple chat application for communication over a local network. This project consists of a server and client scripts written in Python, allowing multiple users to connect and chat with each other.

## Features

- **Server-Client Architecture:** Utilizes a server to manage connections and facilitates communication between multiple clients.
- **Multithreading:** Supports concurrent connections with the use of threads for each client.
- **Cross-Platform:** Compatible with any system that supports Python.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/local-network-chat.git
    ```

2. Navigate to the project directory:

    ```bash
    cd local-network-chat
    ```

3. Run the server script on a machine that will act as the server:

    ```bash
    python server.py
    ```

4. Run the client script on other machines:

    ```bash
    python client.py
    ```

5. Follow the on-screen instructions to connect and chat.

## Usage

- Run the server script on a central machine.
- Run the client script on multiple machines, providing the server's IP address.
- Type messages in the client's console to chat with others.

## Documentation

### Server Documentation (server.py):

```python
"""
Server for Local Network Chat

This script creates a simple chat server that allows multiple clients to connect over a local network and chat with each other.

Usage:
    - Run this script on a machine that will act as the server.
    - Clients connect to the server's IP address and port to participate in the chat.

Requirements:
    - Python 3.x
"""

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

