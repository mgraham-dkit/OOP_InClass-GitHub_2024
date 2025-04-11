import networked_pizzeria.service.pizzeria_service as service
from networked_pizzeria.client.controller import pizzeria_controller
from networked_pizzeria.client.pizzeria_service.services import NetworkedPizzaService, NetworkedOrderService
from networked_pizzeria.client.view.view_manager import Pizzeria
from networked_pizzeria.network.network_service import TcpNetworkLayer

if __name__ == "__main__":
    # Build layers

    # Build the view component - this should not change in a networked system
    view_manager = Pizzeria()

    # Create network layer for model use
    network_layer = TcpNetworkLayer(host=service.HOST, port=service.PORT)

    # Create model objects. By injecting the network layer into each service separately,
    # we allow for each network service to have a separate connection (if they were hosted separately)
    pizza_service = NetworkedPizzaService(network_layer)
    order_service = NetworkedOrderService(network_layer)

    # Set up the controller
    controller = pizzeria_controller.PizzeriaController(view_manager, order_service, pizza_service)

    # Start GUI
    view_manager.run()
