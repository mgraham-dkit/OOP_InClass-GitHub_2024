import socket

import networked_pizzeria.service.pizzeria_service as service
from networked_pizzeria.client.pizzeria_service.service_interfaces import PizzaInterface
from networked_pizzeria.network.network_service import TcpNetworkLayer
from networked_pizzeria.server.controller.controller import PizzeriaController, PizzeriaClientHandler
from networked_pizzeria.server.model.services import PizzaService, OrderService


class PizzeriaServer:
    def __init__(self, pizza_service: PizzaInterface, order_service: OrderService):
        self.pizza_service = pizza_service
        self.order_service = order_service

    def run(self) -> None:
        server_session = True
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((service.HOST, service.PORT))
            server_socket.listen()

            while server_session:
                conn, addr = server_socket.accept()
                # Create network layer object for client
                client_network_layer = TcpNetworkLayer(data_socket=conn)
                # Clear order state for new client
                self.order_service.clear()
                # Create controller to deal with logic of service
                client_controller = PizzeriaController(self.pizza_service, self.order_service)
                # Create handler to deal with processing request to confirm real
                # (this could be combined with controller)
                pizzeria_client = PizzeriaClientHandler(addr, client_network_layer, client_controller)
                # Kick off client handling
                pizzeria_client.handle_client()

        print("Server shutting down...")


if __name__ == "__main__":
    # Create service/model classes
    injected_pizza_service = PizzaService()
    injected_order_service = OrderService()
    # Create scheduler - No controller is injected here
    # This is so that each client can have its own status and controller flow
    pizzeria_server = PizzeriaServer(injected_pizza_service, injected_order_service)
    # Run server
    pizzeria_server.run()