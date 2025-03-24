import services
import pizzeria_views

class PizzeriaController:
    def __init__(self, pizzeria: pizzeria_views.Pizzeria, order_service: services.OrderService, pizza_service: services.PizzaServce):
        self.view = pizzeria
        self.order_service = order_service
        self.pizza_service = pizza_service

        self.view.set_controller(self)

    # Trigger active view to change (updates view layer, no model involvement)
    def update_view(self, view_name):
        self.view.update_view(view_name)

    # Trigger pizza to be added to order (queries model layer, gets result and passes back to view)
    def add_pizza(self, pizza_name, pizza_size, pizza_toppings):
        pizza, rejected_toppings = self.pizza_service.create_pizza(pizza_name, pizza_size, pizza_toppings)
        self.order_service.add_pizza(pizza)
        return rejected_toppings

    # Retrieve named pizza from order (queries model layer, gets result and passes back to view)
    def get_pizza(self, pizza_name):
        return self.order_service.get_pizza(pizza_name)

    def get_order(self):
        return self.order_service.get_order()
