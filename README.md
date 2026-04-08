# SocketChat - Multi-Client Messaging Application

A real-time chat application using Python TCP Sockets for CMPT-371 Assignment 3.

## Team Member
- **Name**: Daniel  
- **Student ID**: 301428609
- **Email**: dgtutv@gmail.com

## Project Description
Multi-client messaging app with client-server architecture using sockets.  
Supports broadcast messages and private messaging.

## Features
- Multiple concurrent clients (threading)
- Broadcast messages to all users
- Private messaging (`/pm username message`)
- List online users (`/users`)
- Graceful disconnect (`/quit`)

## Limitations
- No end-to-end encryption (plain text messages)
- No message persistence
- CLI interface only
- Single server instance
- Performance depends on network stability

## How to Run (Fresh Environment)

**No additional libraries required** — only standard Python.

1. Start the server in one terminal:
   ```bash
   python server.py```

2. Start clients in separate terminals:Bashpython client.py

Available Commands:

Type any message → broadcast to everyone
/pm username message → send private message
/users → show who is online
/quit → exit the chat
Made for CMPT-371 A3.
