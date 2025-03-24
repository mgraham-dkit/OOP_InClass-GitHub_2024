from food import Order, Pizza
from abc import ABC, abstractmethod


class OrderInterface(ABC):
    @abstractmethod
    def add_pizza(self, pizza):
        pass

    @abstractmethod
    def get_pizza(self, pizza_name):
        pass

    @abstractmethod
    def get_order(self):
        pass


class OrderService(OrderInterface):
    def __init__(self):
        self.order = Order()

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


class PizzaInterface(ABC):
    @abstractmethod
    def create_pizza(self, pizza_name, pizza_size, pizza_desc = "Custom", pizza_toppings = None):
        pass


class PizzaService(PizzaInterface):
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