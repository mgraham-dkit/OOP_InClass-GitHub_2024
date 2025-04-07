import socket
import datetime as dt
import combo_utils as service


FORMAT = "%H:%M:%S:%f, %d/%m/%Y"


def handle_echo(components):
    if len(components) == 2 and components[1]:
        return components[1]

    return service.INVALID


def handle_daytime(components):
    if len(components) == 1:
        current_date_time = dt.datetime.now()
        return current_date_time.strftime(FORMAT)

    return service.INVALID


def handle_stats(components, counter):
    if len(components) == 1:
        return str(counter)

    return service.INVALID


def handle_request(decoded):
    components = decoded.split(service.DELIMITER)
    response = service.INVALID
    match components[0]:
        case service.ECHO:
            response = handle_echo(components)
        case service.DAYTIME:
            response = handle_daytime(components)
        case service.STATS:
            response = handle_stats(components, msg_count)

    return response


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

                response = handle_request(decoded)

                conn.sendall(bytes(response, "utf-8"))

            print(f"Client {addr} disconnected.")