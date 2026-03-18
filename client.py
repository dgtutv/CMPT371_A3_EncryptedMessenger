import socket
import threading

username = input("Enter your username: ").strip() or "Anonymous"
ip = input("Server IP (Enter for localhost): ").strip() or "127.0.0.1"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip, 55555))
client.send(username.encode('utf-8'))

def receive():
    while True:
        try:
            print(client.recv(1024).decode('utf-8'))
        except:
            break

threading.Thread(target=receive, daemon=True).start()

print("Connected! Commands: /pm username msg | /users | /quit")

while True:
    msg = input()
    if msg.lower() == '/quit':
        break
    if msg.strip():
        client.send(msg.encode('utf-8'))

client.close()
