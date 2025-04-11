from tkinter import messagebox
import tkinter as tk

from networked_pizzeria.client.view.pizzeria_views import PizzeriaHomeMenu, CreatePizzaView, PizzeriaSummaryView, View
from networked_pizzeria.client.view.view_options import HOME, CREATE_PIZZA, SUMMARY


class Pizzeria:
    # Set up overall application window
    # Should store the active view and a dictionary of view options
    def __init__(self):
        # Construct core window
        self.window = tk.Tk()
        self.window.title("Pizza Ordering System")
        self.window.geometry("300x150")
        self.window.minsize(300, 150)
        # Specify shutdown behaviour path
        self.window.protocol("WM_DELETE_WINDOW", self.on_shutdown)

        # Set up store for active view
        self.current = None

        # Populate dictionary of available views
        self.views = self.define_views()

        # Build main window - fill with initial view
        self.build()

    def build(self):
        # Set active view to the home view
        self.current = self.views[HOME]
        self.current.show()

        # Ensure the window's size is correct
        # Wait until any changes to window currently in progress are completed
        self.window.update_idletasks()
        # Resize to correct dimensions automatically
        self.window.geometry("")
        # Guarantee it doesn't get too small
        self.window.minsize(300, 150)

    # Set up flexible collection of views
    # This does not build the views, it just creates them
    # Views are built the first time they are requested
    def define_views(self) -> dict[str, View]:
        # Create a dictionary of available views
        # Use constants (HOME, CREATE_PIZZA etc) as keys to standardise their references
        views = {
            HOME: PizzeriaHomeMenu(self.window),
            CREATE_PIZZA: CreatePizzaView(self.window),
            SUMMARY: PizzeriaSummaryView(self.window)
        }

        # Return the collection of views
        return views

    # Method to update the active view
    # Takes in a view name - this should be a class-level constant (static)
    def update_view(self, view_name):
        # Hide current screen
        self.current.hide()
        # If valid view supplied
        if view_name in self.views:
            # Update current screen to create pizza view
            self.current = self.views[view_name]
            # Show selected view
            self.current.show()
        else:
            # Deal with no such view - error 404!
            messagebox.showerror("404 - Invalid View", f"The requested view cannot be found.")
            self.update_view(HOME)

    def set_controller(self, controller):
        for view in self.views.values():
            view.set_controller(controller)

    def on_shutdown(self):
        if self.current:
            self.current.shutdown()
        else:
            self.close()

    def close(self):
        self.window.destroy()

    def run(self):
        # Start main loop on gui - turn GUI on
        self.window.mainloop()