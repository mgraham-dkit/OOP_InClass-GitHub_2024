from networked_pizzeria.client.pizzeria_service import services
from networked_pizzeria.client.view import pizzeria_views
from networked_pizzeria.client.view.view_manager import Pizzeria


class PizzeriaController:
    def __init__(self, pizzeria: Pizzeria, order_service: services.NetworkedOrderService, pizza_service: services.NetworkedPizzaService):
        self.view = pizzeria
        self.order_service = order_service
        self.pizza_service = pizza_service

        self.view.set_controller(self)

    # Trigger active view to change (updates view layer, no model involvement)
    def update_view(self, view_name):
        self.view.update_view(view_name)

    # Request list of all possible topping options from the Model
    def get_topping_options(self):
        return self.pizza_service.get_topping_options()

    # Request list of all possible sizes options from the Model
    def get_size_options(self):
        return self.pizza_service.get_size_options()

    # Trigger pizza to be added to order (Amended to query only pizza service (server side will fold in order process), gets result and passes back to view)
    def add_pizza(self, pizza_name, pizza_size, pizza_toppings):
        rejected_toppings = self.pizza_service.create_pizza(pizza_name, pizza_size, pizza_desc="Custom pizza", pizza_toppings=pizza_toppings)
        return rejected_toppings

    # Retrieve named pizza from order (queries model layer, gets result and passes back to view)
    def get_pizza(self, pizza_name):
        return self.order_service.get_pizza(pizza_name)

    def get_order(self):
        return self.order_service.get_order()

    # Provide method to shut down service network connections & close GUI
    def shutdown(self):
        # Disconnect services from network
        self.order_service.shutdown()
        self.pizza_service.shutdown()

        # Close down view
        # Remember - view can't make the decision to shut, controller has to trigger it!
        self.view.close()
        print("Shutting down...")