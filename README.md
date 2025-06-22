
# 🖧 TCP Server (Python)

A simple Python-based TCP server that accepts incoming connections, receives data from clients, and prints it to the console. Useful for basic network testing, socket programming practice, or as a template for more complex server applications.

---

## 🚀 Features

- Listens on a specified IP and port
- Accepts multiple client connections (sequentially)
- Prints client messages to the console
- Clean, readable socket code using Python’s built-in `socket` module

---

## 🛠️ Requirements

- Python 3.x

No external libraries are required.

---

## 📦 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/anvpeace/tcp_server.git
   cd tcp_server
````

2. Run the server:

   ```bash
   python tcp_server.py
   ```

---

## 🧪 Usage

By default, the server listens on `localhost` and port `12345`. Once running:

1. Use a TCP client (e.g., `telnet`, `nc`, or a custom script) to connect:

   ```bash
   nc localhost 12345
   ```

2. Type a message and press Enter. The server will print your message.

---

## 🧱 Code Structure

* `tcp_server.py`: Contains the main server loop and socket configuration

---

## ⚠️ Disclaimer

This server is for educational and testing use. It accepts raw input and should **not** be used in production without proper security, validation, and concurrency handling.

---

## 📄 License

MIT License. See [`LICENSE`](LICENSE) for details.

```
```

#Code Explaination
    socket is an internal endpoint for sending and recieving data
    
    socket is like an outlet that give connection from grid to transformer to house

    network socket allows you to send and recieve dat because it works locally

    socket library - impliment sockets with different protocols;

    socket module - import to use then call in socket function

    create object then object calls socket function

    socket family - afi net (socket.soc) used to specificy protocol used for communication either IPv4 or IPv6

# socet type - socket stream - specifies connection oriented protocols like TCP(three way handshake)
# UDP uses soc degram

# common methods
 bind
 listen
 accept
 send
 recieve