import socket

import networked_pizzeria.service.pizzeria_service as service
from networked_pizzeria.client.pizzeria_service.service_interfaces import PizzaInterface
from networked_pizzeria.network.network_service import TcpNetworkLayer, ITcpNetworkLayer
from networked_pizzeria.server.controller.controller import PizzeriaController
from networked_pizzeria.server.model.services import PizzaService


class PizzeriaServer:
    def __init__(self, pizza_service: PizzaInterface):
        self.service = pizza_service
    def run(self) -> None:
        server_session = True
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((service.HOST, service.PORT))
            server_socket.listen()

            while server_session:
                conn, addr = server_socket.accept()
                client_network_layer = TcpNetworkLayer(data_socket=conn)
                client_controller = PizzeriaController(pizza_service)
                pizzeria_client = PizzeriaClientHandler(addr, client_network_layer, client_controller)
                pizzeria_client.handle_client()

        print("Server shutting down...")


class PizzeriaClientHandler:
    def __init__(self, addr: tuple[str, int], network_layer: ITcpNetworkLayer, controller: PizzeriaController):
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
    # Create service/model classes
    pizza_service = PizzaService()
    # Create scheduler - No controller is injected here
    # This is so that each client can have its own status and controller flow
    pizzeria_server = PizzeriaServer(pizza_service)
    # Run server
    pizzeria_server.run()