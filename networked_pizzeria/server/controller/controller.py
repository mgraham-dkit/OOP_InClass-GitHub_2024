from __future__ import annotations
import networked_pizzeria.service.pizzeria_service as service
from networked_pizzeria.client.pizzeria_service.service_interfaces import PizzaInterface
from networked_pizzeria.network.network_service import ITcpNetworkLayer


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


class PizzeriaController:
    def __init__(self, pizza_service: PizzaInterface):
        self.pizza_service = pizza_service

    def handle_request(self, decoded: str) -> str:
        components = decoded.split(service.BASE_DELIMITER)
        response = service.INVALID
        match components[0]:
            case service.TOPPINGS:
                response = self.handle_get_toppings(components)
            case service.SIZES:
                response = self.handle_get_sizes(components)

        return response

    def handle_get_toppings(self, components):
        # Validate request structure - return appropriate error if issue is detected
        if len(components) != 1:
            return service.INVALID

        # Ask model to carry out requested action and store returned result
        toppings = self.pizza_service.get_topping_options()

        # Convert result to protocol-specific structure for transmission & return to handler
        return service.TOPPING_DELIMITER.join(toppings)

    def handle_get_sizes(self, components):
        # Validate request structure - return appropriate error if issue is detected
        if len(components) != 1:
            return service.INVALID

        # Ask model to carry out requested action and store returned result
        sizes = self.pizza_service.get_size_options()

        # Convert result to protocol-specific structure for transmission & return to handler
        return service.BASE_DELIMITER.join(sizes)
