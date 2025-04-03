import socket
import datetime as dt
import maths_utils as service

class MathsServer:
    def __init__(self):
        self.largest = None
        self.isActive = True

    def update_largest(self, result):
        if self.largest is None:
            self.largest = result

        if result > self.largest:
            self.largest = result


    def run(self):
        # Most of the code below can be used as a template to structure servers
        # The service-specific code (i.e. the code that changes from service to service)
        # is surrounded by comment lines
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((service.HOST, service.PORT))
            server_socket.listen()

            while self.isActive:
                conn, addr = server_socket.accept()
                with conn:
                    client_session = True

                    while client_session:
                        largest = None
                        print(f"Waiting for message from {addr}")
                        data = conn.recv(1024)
                        if not data:
                            client_session = False
                            continue

                        decoded = data.decode("utf-8")
                        print(f"Message received from {addr}: {decoded}")

                        ######## BEGIN SERVICE LOGIC #########
                        response = self.handle_request(decoded)
                        ######## END SERVICE LOGIC #########

                        print(f"Sending response: \"{response}\"")
                        conn.sendall(bytes(response, "utf-8"))

                    print(f"Client {addr} disconnected.")

    def handle_request(self, decoded):
        components = decoded.split(service.DELIMITER)
        response = service.UNKNOWN
        match components[0]:
            case service.SQUARE:
                response = self.handle_square(components)
            case service.CUBE:
                response = self.handle_cube(components)
            case service.LARGEST:
                response = self.handle_largest(components)
        return response

    def handle_cube(self, components):
        if len(components) == 2:
            try:
                value = float(components[1])
            except ValueError as e:
                # LOG error, don't just print
                print(f"Cannot convert \"{components[1]}\" to float")
                return service.NO_NUMBER

            result = value * value * value

            self.update_largest(result)
            return str(result)

        return service.UNKNOWN

    def handle_square(self, components):
        if len(components) == 2:
            try:
                value = float(components[1])
            except ValueError as e:
                # LOG error, don't just print
                print(f"Cannot convert \"{components[1]}\" to float")
                return service.NO_NUMBER

            result = value * value

            self.update_largest(result)
            return str(result)

        return service.UNKNOWN

    def handle_largest(self, components):
        if len(components) == 1:
            return str(self.largest)

        return service.UNKNOWN

if __name__ == "__main__":
    server = MathsServer()
    server.run()