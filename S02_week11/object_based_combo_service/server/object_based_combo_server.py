import socket

from S02_week11.object_based_combo_service.network.network_service import TcpNetworkLayer, ITcpNetworkLayer
import S02_week11.object_based_combo_service.service.combo_utils as service
from controller import ComboController


class ComboServer:
    def __init__(self, controller: ComboController):
        self.controller = controller

    def run(self) -> None:
        server_session = True
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((service.HOST, service.PORT))
            server_socket.listen()

            while server_session:
                conn, addr = server_socket.accept()
                client_network_layer = TcpNetworkLayer(conn)
                combo_client = ComboClientHandler(addr, client_network_layer, self.controller)
                combo_client.handle_client()

        print("Server shutting down...")


class ComboClientHandler:
    def __init__(self, addr: tuple[str, int], network_layer: ITcpNetworkLayer, controller: ComboController):
        self.addr = addr
        self.network_layer = network_layer
        self.controller = controller

    def handle_client(self) -> None:
        client_session = True
        while client_session:
            print(f"Waiting for message from {self.addr}")
            data = self.network_layer.receive()
            if not data:
                client_session = False
                continue

            decoded = data.decode("utf-8")
            print(f"Message received from {self.addr}: {decoded}")

            response = self.controller.handle_request(decoded)

            self.network_layer.send(response)
        self.network_layer.disconnect()
        print(f"Client {self.addr} disconnected.")


if __name__ == "__main__":
    injected_controller = ComboController()
    combo_server = ComboServer(injected_controller)
    combo_server.run()