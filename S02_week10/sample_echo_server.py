import socket

HOST = "127.0.0.1"
PORT = 7878

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))

    server_socket.listen()

    while True:
        conn, addr = server_socket.accept()

        with conn:
            data = conn.recv(1024)
            decoded = data.decode("utf-8")
            print(f"Message received from {addr}: {decoded}")

            conn.sendall(bytes(decoded, "utf-8"))