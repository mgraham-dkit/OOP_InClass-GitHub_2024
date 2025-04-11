import networked_pizzeria.service.pizzeria_service as service
from networked_pizzeria.client.pizzeria_service.service_interfaces import OrderInterface, PizzaInterface
from networked_pizzeria.entities.food import Order, Pizza
from networked_pizzeria.network.network_service import ITcpNetworkLayer


class NetworkedOrderService(OrderInterface):
    def __init__(self, network_layer: ITcpNetworkLayer):
        self.order = Order()
        self.network_layer = network_layer

    def add_pizza(self, pizza):
        self.order.add_item(pizza)

    def get_pizza(self, pizza_name):
        return self.order.get_item(pizza_name)

    def get_order(self):
        if not self.order:
            return "Your order is empty."

        order_summary = "Your Order:\n\n"
        for name, pizza in self.order.items.items():
            toppings = pizza.get_toppings()
            order_summary += f"{name}: {pizza.get_size().capitalize()} with {', '.join(toppings) if toppings else 'no toppings'} - €{pizza.calc_price()}\n"

        order_summary += f"\nTotal: €{self.order.calc_price()}"
        return order_summary

    def shutdown(self):
        if self.network_layer.is_connected():
            self.network_layer.disconnect()


class NetworkedPizzaService(PizzaInterface):
    def __init__(self, network_layer: ITcpNetworkLayer):
        self.network_layer = network_layer

    def create_pizza(self, pizza_name, pizza_size, pizza_desc = "Custom", pizza_toppings = None):
        if not Pizza.validate_size(pizza_size):
            pizza_size = "medium"

        if pizza_toppings is None:
            pizza_toppings = []

        pizza = Pizza(pizza_name, pizza_desc=pizza_desc, size=pizza_size)
        print(f"Name: {pizza.name}")
        rejected_toppings = []
        for topping in pizza_toppings:
            added = pizza.add_topping(topping)
            if not added:
                rejected_toppings.append(topping)

        return pizza, rejected_toppings

    def get_topping_options(self):
        # Send request
        request = service.TOPPINGS
        self.network_layer.send(request)
        # Get response
        response = self.network_layer.receive()
        # Parse to text
        decoded = response.decode("utf-8")
        # Parse out of protocol format
        toppings = decoded.split(service.TOPPING_DELIMITER)
        # Return result
        return toppings

    def get_size_options(self) -> list[str]:
        # Send request
        request = service.SIZES
        self.network_layer.send(request)
        # Get response
        response = self.network_layer.receive()
        # Parse to text
        decoded = response.decode("utf-8")
        # Parse out of protocol format
        sizes = decoded.split(service.BASE_DELIMITER)
        # Return result
        return sizes

    def shutdown(self):
        if self.network_layer.is_connected():
            self.network_layer.disconnect()