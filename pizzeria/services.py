from food import Order, Pizza


class OrderService:
    def __init__(self):
        self.active_order = Order()

    def add_pizza(self, pizza_name, pizza_size, pizza_desc = "Custom", pizza_toppings = None):
        if not Pizza.validate_size(pizza_size):
            pizza_size = "medium"

        if pizza_toppings is None:
            pizza_toppings = []

        pizza = Pizza(pizza_name, pizza_desc, pizza_size)

        rejected_toppings = []
        for topping in pizza_toppings:
            added = pizza.add_topping(topping)
            if not added:
                rejected_toppings.append(topping)


        self.active_order.add_item(pizza)
        return rejected_toppings

    def get_pizza(self, pizza_name):
        return self.active_order.get_item(pizza_name)
