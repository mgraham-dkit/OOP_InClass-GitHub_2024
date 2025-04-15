from abc import ABC, abstractmethod


class OrderInterface(ABC):
    @abstractmethod
    def get_pizza(self, pizza_name):
        pass

    @abstractmethod
    def get_order(self):
        pass

class PizzaInterface(ABC):
    @abstractmethod
    def create_pizza(self, pizza_name, pizza_size, pizza_desc = "Custom", pizza_toppings = None):
        pass

    @abstractmethod
    def get_topping_options(self):
        pass

    @abstractmethod
    def get_size_options(self):
        pass
