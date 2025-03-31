import socket

HOST = "127.0.0.1"
PORT = 11777
keep_running = True

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))

    while keep_running:
        msg = input("Enter a message to be sent (-1 to end): ")
        if msg == "-1":
            keep_running = False
            continue

        client_socket.sendall(bytes(msg, "utf-8"))
        print("Data sent.")

        data = client_socket.recv(1024)
        print(f"Received: {data.decode('utf-8')}")

print("Connection terminated.")
