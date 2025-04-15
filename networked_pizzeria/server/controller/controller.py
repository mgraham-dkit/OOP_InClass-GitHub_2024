from __future__ import annotations
import networked_pizzeria.service.pizzeria_service as service
from networked_pizzeria.client.pizzeria_service.service_interfaces import PizzaInterface
from networked_pizzeria.exceptions.pizzeria_exceptions import UnknownSizeError
from networked_pizzeria.network.network_service import ITcpNetworkLayer
from networked_pizzeria.server.model.services import OrderService


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

            print(f"Message received from {self.addr}: {data}")

            response = self.controller.handle_request(data)

            self.network_layer.send(response)
        self.network_layer.disconnect()
        print(f"Client {self.addr} disconnected.")


class PizzeriaController:
    def __init__(self, pizza_service: PizzaInterface, order_service: OrderService):
        self.pizza_service = pizza_service
        self.order_service = order_service

    def handle_request(self, decoded: str) -> str:
        print(f"Request: '{decoded}'")
        components = decoded.split(service.BASE_DELIMITER)
        response = service.UNKNOWN
        match components[0]:
            case service.TOPPINGS:
                response = self.handle_get_toppings(components)
            case service.SIZES:
                response = self.handle_get_sizes(components)
            case service.CREATE:
                response = self.handle_create_pizza(components)
            case service.GET_PIZZA:
                response = self.handle_get_pizza(components)
            case service.GET_ORDER:
                response = self.handle_get_order(components)

        return response

    def handle_get_toppings(self, components: list[str]) -> str:
        # Validate request structure - return appropriate error if issue is detected
        if len(components) != 1:
            return service.UNKNOWN

        # Ask model to carry out requested action and store returned result
        toppings = self.pizza_service.get_topping_options()

        # Convert result to protocol-specific structure for transmission & return to handler
        return service.TOPPING_DELIMITER.join(toppings)

    def handle_get_sizes(self, components: list[str]) -> str:
        # Validate request structure - return appropriate error if issue is detected
        if len(components) != 1:
            return service.UNKNOWN

        # Ask model to carry out requested action and store returned result
        sizes = self.pizza_service.get_size_options()

        # Convert result to protocol-specific structure for transmission & return to handler
        return service.BASE_DELIMITER.join(sizes)

    def handle_create_pizza(self, components: list[str]) -> str:
        if len(components) != 5:
            return service.UNKNOWN

        # structure: CREATE%%$name%%$desc%%$size%%$topping[~~$topping]*
        # Extract the component pieces
        pizza_name = components[1]
        pizza_desc = components[2]
        pizza_size = components[3]
        pizza_toppings = components[4].split(service.TOPPING_DELIMITER)

        try:
            # Attempt to build a pizza
            pizza, rejected_toppings = self.pizza_service.create_pizza(pizza_name, pizza_size, pizza_desc, pizza_toppings)
            # If the attempt didn't fail, add it to the order
            self.order_service.add_pizza(pizza)
            print(f"Added pizza: {pizza}")

            # Build response from valid result
            if len(rejected_toppings) == 0:
                return service.NO_REJECTED
            else:
                return service.TOPPING_DELIMITER.join(rejected_toppings)

        # Handle where size information was invalid
        except UnknownSizeError as e:
            return service.INVALID_SIZE

    def handle_get_pizza(self, components: list[str]) -> str:
        if len(components) != 2:
            return service.UNKNOWN

        pizza = self.order_service.get_pizza(components[1])
        if not pizza:
            return service.INVALID_NAME

        return self.format_pizza_response(pizza)

    def handle_get_order(self, components: list[str]) -> str:
        if len(components) != 1:
            return service.UNKNOWN

        order = self.order_service.get_order()

        if not order.items:
            return service.EMPTY_ORDER

        pizza_strings = []
        for item in order.items.values():
            pizza_string = self.format_pizza_response(item)
            pizza_strings.append(pizza_string)

        return service.SECTION_DELIMITER.join(pizza_strings)

    def format_pizza_response(self, pizza: Pizza) -> str:
        accepted_toppings = service.TOPPING_DELIMITER.join(pizza.get_toppings())
        pizza_list = [pizza.name, pizza.desc, pizza.get_size(), accepted_toppings]
        return service.BASE_DELIMITER.join(pizza_list)
