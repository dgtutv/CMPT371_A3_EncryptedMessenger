import socket
import threading

clients = []
usernames = {}

def broadcast(message: bytes):
    for client in clients[:]:
        try:
            client.send(message)
        except:
            remove_client(client)

def remove_client(client):
    if client in clients:
        clients.remove(client)
        if client in usernames:
            username = usernames.pop(client)
            broadcast(f"{username} has left the chat.".encode('utf-8'))
        try: client.close() except: pass

def handle_client(client):
    try:
        username = client.recv(1024).decode('utf-8').strip() or "Anonymous"
        usernames[client] = username
        broadcast(f"{username} has joined the chat!".encode('utf-8'))
    except:
        remove_client(client)
        return

    while True:
        try:
            msg = client.recv(1024)
            if not msg: break
            text = msg.decode('utf-8').strip()
            if text.lower() == '/quit':
                break
            elif text.startswith('/pm '):
                parts = text.split(' ', 2)
                if len(parts) < 3: 
                    client.send(b"Usage: /pm username message")
                    continue
                target = parts[1]
                pm = parts[2]
                for c, u in list(usernames.items()):
                    if u.lower() == target.lower():
                        c.send(f"[Private from {username}] {pm}".encode('utf-8'))
                        client.send(f"[Private to {target}] {pm}".encode('utf-8'))
                        return
                client.send(f"User '{target}' not found.".encode('utf-8'))
            elif text == '/users':
                users = ", ".join(usernames.values()) or "No one online"
                client.send(f"Online: {users}".encode('utf-8'))
            else:
                broadcast(f"{username}: {text}".encode('utf-8'))
        except:
            break
    remove_client(client)

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('0.0.0.0', 55555))
    s.listen()
    print("[SERVER] SocketChat started on port 55555")
    while True:
        client, addr = s.accept()
        clients.append(client)
        threading.Thread(target=handle_client, args=(client,), daemon=True).start()
