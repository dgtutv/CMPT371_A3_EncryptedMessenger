# followed Sam Codes tutorial series https://www.youtube.com/watch?v=zENAxBPQHCo&list=PLWnON6N0wn-FXZ0ECb9iSAZwWoeGr1rUp&index=1&pp=iAQB

import threading
import socket
import argparse
import os

class Server(threading.Thread):
    
    def __init__(self, host, port):
        super().__init__()
        self.connections = []
        self.host = host
        self.port = port
        
    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((self.host, self.port))
        
        sock.listen(1)
        print("Listening at: ", sock.getsockname())
        
        while True:
            # Accepting new connection
            sc, sockname = sock.accept()
            print(f"Accepting a new connection from {sc.getpeername()} to {sc.getsockname()}")
            
            # Create a new thread
            sever_socket = ServerSocket(sc, sockname, self)
            
            # Stasrt new thread
            server_socket.start()
            
            # Add thread to active connection
            self.cocnnections.append(server_socket)
            print("Ready to receive messages from: ", sc.getpeername())
            
    def broadcast(self, message, source):
        for connection in self.connections:
            # send to all connected client accept the source client
            if connection.sockname != source:
                connection.send(message)
                
    def remove_connection(self, connection):
        self.connections.remove(connection)