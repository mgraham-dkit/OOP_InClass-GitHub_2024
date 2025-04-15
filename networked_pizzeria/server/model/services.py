from networked_pizzeria.client.pizzeria_service.service_interfaces import PizzaInterface, OrderInterface
from networked_pizzeria.entities.food import Order, Pizza
from networked_pizzeria.exceptions.pizzeria_exceptions import UnknownSizeError


class OrderService(OrderInterface):
    def __init__(self):
        self.order = Order()

    def add_pizza(self, pizza: Pizza) -> None:
        self.order.add_item(pizza)

    def get_pizza(self, pizza_name: str) -> Pizza:
        return self.order.get_item(pizza_name)

    def get_order(self) -> Order:
        return self.order

    def clear(self) -> None:
        self.order = Order()
    

class PizzaService(PizzaInterface):
    def create_pizza(self, pizza_name: str, pizza_size: str, pizza_desc: str = "Custom", pizza_toppings: list[str] = None):
        print(f"Size: '{pizza_size}'")
        if not Pizza.validate_size(pizza_size):
            raise UnknownSizeError(f"Illegal size requested - {pizza_size} is not a recognised size in the system.")

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

    def get_topping_options(self) -> list[str]:
        return Pizza.topping_options

    def get_size_options(self) -> list[str]:
        return Pizza.size_options