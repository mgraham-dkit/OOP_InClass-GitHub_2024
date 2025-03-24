import pizzeria_controller
import pizzeria_views
import services

# Build layers
view = pizzeria_views.Pizzeria()
order_model = services.OrderService()
pizza_model = services.PizzaServce()
controller = pizzeria_controller.PizzeriaController(view, order_model, pizza_model)

# Start GUI
view.run()
