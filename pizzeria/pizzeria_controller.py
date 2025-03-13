import services
import pizzeria_views

class PizzeriaController:
    def __init__(self, pizzeria: pizzeria_views.Pizzeria, pizza_service: services.OrderService):
        self.view = pizzeria
        self.service = pizza_service

        self.view.set_controller(self)

    # Trigger active view to change (updates view layer, no model involvement)
    def update_view(self, view_name):
        self.view.update_view(view_name)

    # Trigger pizza to be added to order (queries model layer, gets result and passes back to view)
    def add_pizza(self, pizza_name, pizza_size, pizza_toppings):
        return self.service.add_pizza(pizza_name, pizza_size, pizza_toppings)

    # Retrieve named pizza from order (queries model layer, gets result and passes back to view)
    def get_pizza(self, pizza_name):
        return self.service.get_pizza(pizza_name)
