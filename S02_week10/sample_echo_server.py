import socket

HOST = "127.0.0.1"
PORT = 11777

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))

    server_socket.listen()

    while True:
        conn, addr = server_socket.accept()
        with conn:
            client_session = True

            while client_session:
                print(f"Waiting for message from {addr}")
                data = conn.recv(1024)
                if not data:
                    client_session = False
                    continue

                decoded = data.decode("utf-8")
                print(f"Message received from {addr}: {decoded}")

                components = decoded.split("%%")
                response = "INVALID"
                match components[0]:
                    case "ECHO":
                        if len(components) == 2 and components[1]:
                            response = components[1]

                conn.sendall(bytes(response, "utf-8"))

            print(f"Client {addr} disconnected.")