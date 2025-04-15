import networked_pizzeria.service.pizzeria_service as service
from networked_pizzeria.client.pizzeria_service.service_interfaces import OrderInterface, PizzaInterface
from networked_pizzeria.entities.food import Order, Pizza
from networked_pizzeria.exceptions.pizzeria_exceptions import UnknownResponse
from networked_pizzeria.network.network_service import ITcpNetworkLayer


class NetworkedOrderService(OrderInterface):
    def __init__(self, network_layer: ITcpNetworkLayer):
        self.network_layer = network_layer

    def get_pizza(self, pizza_name: str) -> Pizza:
        request = service.GET_PIZZA + service.BASE_DELIMITER + pizza_name
        self.network_layer.send(request)

        response = self.network_layer.receive()
        pizza_components = response.split(service.BASE_DELIMITER)
        topping_components = pizza_components[3].split(service.TOPPING_DELIMITER)
        pizza = Pizza(pizza_components[0], pizza_components[1], pizza_components[2], topping_components)
        return pizza

    def get_order(self) -> str:
        request = service.GET_ORDER
        self.network_layer.send(request)

        response = self.network_layer.receive()
        if response == service.EMPTY_ORDER:
            return "Your order is empty."

        order = self.parse_order(response)

        order_summary = "Your Order:\n\n"
        for name, pizza in order.items.items():
            toppings = pizza.get_toppings()
            order_summary += f"{name}: {pizza.get_size().capitalize()} with {', '.join(toppings) if toppings else 'no toppings'} - €{pizza.calc_price()}\n"

        order_summary += f"\nTotal: €{order.calc_price()}"
        return order_summary

    def shutdown(self) -> None:
        if self.network_layer.is_connected():
            self.network_layer.disconnect()

    def parse_order(self, msg: str) -> Order:
        order = Order()
        pizza_lines = msg.split(service.SECTION_DELIMITER)
        for line in pizza_lines:
            pizza_components = line.split(service.BASE_DELIMITER)
            if len(pizza_components) == 4:
                toppings = pizza_components[3].split(service.TOPPING_DELIMITER)
                pizza = Pizza(pizza_components[0], pizza_components[1], pizza_components[2], toppings)
                order.add_item(pizza)
            else:
                print(f"Malformed line: '{line}'")

        return order


class NetworkedPizzaService(PizzaInterface):
    def __init__(self, network_layer: ITcpNetworkLayer):
        self.network_layer = network_layer

    def create_pizza(self, pizza_name, pizza_size, pizza_desc = "Custom", pizza_toppings = None) -> list[str]:
        if pizza_toppings is None:
            pizza_toppings = []

        # Break objects down into formatted strings (marshall/serialise the data) for transmission
        request_toppings = service.TOPPING_DELIMITER.join(pizza_toppings)
        request_components = [service.CREATE, pizza_name, pizza_desc, pizza_size, request_toppings]
        request = service.BASE_DELIMITER.join(request_components)

        # Send formatted request string
        print(f"Request: {request}")
        self.network_layer.send(request)

        # Wait for response
        response = self.network_layer.receive()

        # Handle if the server didn't understand the request
        if response == service.UNKNOWN:
            raise UnknownResponse(f"{service.UNKNOWN} received for {service.CREATE} request")

        if response == service.NO_REJECTED:
            return []

        # Handle extracting the rejected toppings
        rejected_toppings = response.split(service.TOPPING_DELIMITER)
        return rejected_toppings

    def get_topping_options(self) -> list[str]:
        # Send request
        request = service.TOPPINGS
        self.network_layer.send(request)
        # Get response
        response = self.network_layer.receive()
        # Parse out of protocol format
        toppings = response.split(service.TOPPING_DELIMITER)
        # Return result
        return toppings

    def get_size_options(self) -> list[str]:
        # Send request
        request = service.SIZES
        self.network_layer.send(request)
        # Get response
        response = self.network_layer.receive()
        # Parse out of protocol format
        sizes = response.split(service.BASE_DELIMITER)
        # Return result
        return sizes

    def shutdown(self) -> None:
        if self.network_layer.is_connected():
            self.network_layer.disconnect()