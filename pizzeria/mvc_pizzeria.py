import pizzeria_controller
import pizzeria_views
import services

# Build layers
view = pizzeria_views.Pizzeria()
model = services.OrderService()
controller = pizzeria_controller.PizzeriaController(view, model)

# Start GUI
view.run()