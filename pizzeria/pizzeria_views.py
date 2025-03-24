import tkinter as tk
from abc import ABC, abstractmethod
from tkinter import messagebox

from food import Pizza
import pizzeria_controller


class View(ABC):
    def __init__(self, window):
        self.frame = tk.Frame(window)
        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    # Display this view in the main window
    def show(self):
        # Refresh the content of the view before showing it
        self.refresh()
        self.frame.pack()

    # Hide this view in the main window
    def hide(self):
        self.frame.pack_forget()

    # Implement a default refresh action that does nothing
    def refresh(self):
        pass

    @abstractmethod
    def build(self):
        pass


class PizzeriaHomeMenu(View):
    # STANDARD FEATURES MOVED TO ABSTRACT SUPER/BASE CLASS
    def __init__(self, window):
        super().__init__(window)

        # Individual - unique to this view
        self.add_button = tk.Button(self.frame, text="Add Pizza", command=self.show_pizza_menu, width=20)
        self.finish_button = tk.Button(self.frame, text="Finish Order", command=self.show_summary, width=20)

    # Pack components into view - design!
    # This overrides the abstract method in the abstract super class
    def build(self):
        self.add_button.pack(pady=5)
        self.finish_button.pack(pady=5)

    # VIEW-SPECIFIC FEATURES
    def show_pizza_menu(self):
        # Update the main window to hide this view and show the next one
        self.controller.update_view(Pizzeria.CREATE_PIZZA)

    def show_summary(self):
        # Update the main window to hide this view and show the next one
        self.controller.update_view(Pizzeria.SUMMARY)


class CreatePizzaView(View):
    # STANDARD FEATURES
    # Set up components in view
    def __init__(self, window):
        super().__init__(window)

        # Individual - unique to this view
        # Name data
        self.pizza_name_label = tk.Label(self.frame, text="Enter your pizza's name:")
        self.pizza_name_entry = tk.Entry(self.frame, width=30)

        # Size data
        self.size_var = tk.StringVar()
        self.size_label = tk.Label(self.frame, text="Select a Size:")
        self.size_frame = tk.Frame(self.frame)
        self.set_sizes()

        # Toppings data storage
        self.selected_toppings = []

        # Toppings-related widgets
        self.toppings_label = tk.Label(self.frame, text="Available Toppings:")
        self.toppings_list = tk.Listbox(self.frame, height=5, width=30)
        self.toppings_frame = tk.Frame(self.frame)

        self.set_toppings()

        # Create pizza action
        self.create_button = tk.Button(self.frame, text="Confirm", command=self.create_pizza)

    # Pack components into view - design!
    def build(self):
        # Name
        self.pizza_name_label.grid(row=0, column=0, sticky="w")
        self.pizza_name_entry.grid(row=0, column=1, pady=5, sticky="w")

        # Size
        self.size_label.grid(row=1, column=0, sticky="w")
        self.size_frame.grid(row=1, column=1, pady=5, sticky="w")

        # Toppings
        self.toppings_label.grid(row=2, column=0, sticky="w")
        self.toppings_list.grid(row=3, column=0, columnspan=2, pady=5, sticky="w")
        self.toppings_frame.grid(row=4, column=0, columnspan=2, pady=5, sticky="w")

        # Create pizza button
        self.create_button.grid(row=5, column=0, columnspan=2, pady=10)

    def refresh(self):
        # Clean up previous pizza creations
        self.selected_toppings = []
        self.toppings_list.delete(0, tk.END)
        self.size_var.set("1")
        self.pizza_name_entry.delete(0, tk.END)

    def set_sizes(self):
        for size in Pizza.size_options:
            tk.Radiobutton(self.size_frame, text=size.capitalize(), variable=self.size_var, value=size).pack(
                side="left")

        self.size_var.set("1")

    def set_toppings(self):
        for i, topping in enumerate(Pizza.topping_options):
            row = i // 3
            col = i % 3
            button = tk.Button(
                self.toppings_frame,
                text=topping.capitalize(),
                width=15,
                command=lambda t=topping: self.add_topping(t))

            button.grid(row=row, column=col, padx=5, pady=5)

    # VIEW-SPECIFIC FEATURES
    def add_topping(self, topping):
        if topping not in self.selected_toppings:
            self.selected_toppings.append(topping)
            self.toppings_list.insert(tk.END, topping.capitalize())

    def create_pizza(self):
        pizza_name = self.pizza_name_entry.get()
        size = self.size_var.get()

        if not pizza_name or not size:
            messagebox.showwarning("Missing Information", "Please enter a name and select a size.")
            return

        # Pass control to controller - let it pass the pizza data to the service
        # View deals with displaying the result
        rejected_toppings = self.controller.add_pizza(pizza_name, pizza_size=size, pizza_toppings=self.selected_toppings)
        if rejected_toppings:
            # Display all toppings that could not be added
            messagebox.showwarning("Rejected Toppings",
                                   f"The following toppings could not be added: {', '.join(rejected_toppings)}")

        # Display info on created pizza to user
        self.display_created_pizza_info()

        # Trigger controller to change view to home screen
        self.controller.update_view(Pizzeria.HOME)

    def display_created_pizza_info(self):
        pizza_name = self.pizza_name_entry.get()
        # Request information on the created pizza from the controller
        created_pizza = self.controller.get_pizza(pizza_name)
        messagebox.showinfo("Pizza Created", f"You have ordered: {created_pizza} for €{created_pizza.calc_price()}")


class PizzeriaSummaryView(View):
    # STANDARD FEATURES MOVED TO ABSTRACT SUPER/BASE CLASS
    def __init__(self, window):
        super().__init__(window)

        # Individual - unique to this view
        self.summary_label = tk.Label(self.frame, text="Order Summary:")
        self.order_details = tk.Label(self.frame)

    # Pack components into view - design!
    # This overrides the abstract method in the abstract super class
    def build(self):
        self.summary_label.grid(row=0, column=0, pady=5, sticky="N")
        self.order_details.grid(row=1, column=0, pady=5, sticky="E")

    # This overrides the default refresh action, as it needs to refresh the summary text before being displayed
    def refresh(self):
        summary = self.controller.get_order()
        # Update the text in the summary window
        self.order_details["text"] = summary


class Pizzeria:
    # Establish constants as view names
    HOME = "home"
    CREATE_PIZZA = "create_pizza"
    SUMMARY = "summary"

    # Set up overall application window
    # Should store the active view and a dictionary of view options
    def __init__(self):
        # Construct core window
        self.window = tk.Tk()
        self.window.title("Pizza Ordering System")
        self.window.geometry("300x150")
        self.window.minsize(300, 150)
        # Set up store for active view
        self.current = None

        # Populate dictionary of available views
        self.views = self.define_views()

        # Build main window - fill with initial view
        self.build()

    def build(self):
        # Set active view to the home view
        self.current = self.views[Pizzeria.HOME]
        self.current.show()

        # Ensure the window's size is correct
        # Wait until any changes to window currently in progress are completed
        self.window.update_idletasks()
        # Resize to correct dimensions automatically
        self.window.geometry("")
        # Guarantee it doesn't get too small
        self.window.minsize(300, 150)

    # Set up flexible collection of views
    def define_views(self) -> dict[str, View]:
        # Create a dictionary of available views
        # Use constants (HOME, CREATE_PIZZA etc) as keys to standardise their references
        views = {
            Pizzeria.HOME: PizzeriaHomeMenu(self.window),
            Pizzeria.CREATE_PIZZA: CreatePizzaView(self.window),
            Pizzeria.SUMMARY: PizzeriaSummaryView(self.window)
        }

        # Build all views in the system - this will not make them visible!
        for view in views.values():
            view.build()

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
            self.update_view(Pizzeria.HOME)

    def set_controller(self, controller: pizzeria_controller):
        for view in self.views.values():
            view.set_controller(controller)

    def run(self):
        # Start main loop on gui - turn GUI on
        self.window.mainloop()