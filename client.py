import socket
import threading

# Get username and connect to server
username = input("Enter your username: ").strip() or "Anonymous"
server_ip = input("Server IP (press Enter for localhost): ").strip() or "127.0.0.1"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip, 55555))
client.send(username.encode('utf-8'))

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message:
                print(message)
            else:
                break
        except:
            print("\n[ERROR] Lost connection to server.")
            break

# Start receiving messages in background
threading.Thread(target=receive_messages, daemon=True).start()

print("\nConnected successfully! You can now chat.")
print("Commands:")
print("  /pm <username> <message>   → Private message")
print("  /users                     → List online users")
print("  /quit                      → Leave chat\n")

# Main loop for sending messages
while True:
    message = input("")
    if message.lower() == '/quit':
        client.send(b'/quit')
        break
    if message.strip():
        client.send(message.encode('utf-8'))

client.close()
