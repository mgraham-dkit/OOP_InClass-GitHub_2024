import socket
import datetime as dt
import combo_utils as service


FORMAT = "%H:%M:%S:%f, %d/%m/%Y"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((service.HOST, service.PORT))

    server_socket.listen()
    msg_count = 0

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

                msg_count += 1
                decoded = data.decode("utf-8")
                print(f"Message received from {addr}: {decoded}")

                components = decoded.split(service.DELIMITER)
                response = service.INVALID
                match components[0]:
                    case service.ECHO:
                        if len(components) == 2 and components[1]:
                            response = components[1]
                    case service.DAYTIME:
                        if len(components) == 1:
                            current_date_time = dt.datetime.now()
                            response = current_date_time.strftime(FORMAT)
                    case service.STATS:
                        if len(components) == 1:
                            response = str(msg_count)

                conn.sendall(bytes(response, "utf-8"))

            print(f"Client {addr} disconnected.")