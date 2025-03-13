import tkinter as tk
from tkinter import messagebox, ttk
from food import Pizza
from services import OrderService


def create_pizza():
    pizza_window = tk.Toplevel()
    pizza_window.title("Create Pizza")
    pizza_window.geometry("500x600")

    frame = tk.Frame(pizza_window, padx=10, pady=10)
    frame.pack(fill="both", expand=True)

    tk.Label(frame, text="Enter your pizza's name:").grid(row=0, column=0, sticky="w")
    name_entry = tk.Entry(frame, width=30)
    name_entry.grid(row=0, column=1, pady=5, sticky="w")

    size_var = tk.StringVar()
    tk.Label(frame, text="Select a Size:").grid(row=1, column=0, sticky="w")
    size_frame = tk.Frame(frame)
    size_frame.grid(row=1, column=1, pady=5, sticky="w")
    for size in Pizza.size_options:
        tk.Radiobutton(size_frame, text=size.capitalize(), variable=size_var, value=size).pack(side="left")

    size_var.set("1")

    selected_toppings = []

    def add_topping(topping):
        if topping not in selected_toppings:
            selected_toppings.append(topping)
            toppings_list.insert(tk.END, topping.capitalize())

    tk.Label(frame, text="Available Toppings:").grid(row=2, column=0, sticky="w")
    toppings_list = tk.Listbox(frame, height=5, width=30)
    toppings_list.grid(row=3, column=0, columnspan=2, pady=5, sticky="w")

    toppings_frame = tk.Frame(frame)
    toppings_frame.grid(row=4, column=0, columnspan=2, pady=5, sticky="w")

    for i, topping in enumerate(Pizza.topping_options):
        row = i // 3
        col = i % 3
        tk.Button(
            toppings_frame,
            text=topping.capitalize(),
            width=15,
            command=lambda t=topping: add_topping(t)
        ).grid(row=row, column=col, padx=5, pady=5)

    def confirm():
        pizza_name = name_entry.get()
        size = size_var.get()
        if not pizza_name or not size:
            messagebox.showwarning("Missing Information", "Please enter a name and select a size.")
            return

        rejected_toppings = order_service.add_pizza(pizza_name, pizza_size=size, pizza_toppings=selected_toppings)
        if rejected_toppings:
            messagebox.showwarning("Rejected Toppings",
                                   f"The following toppings could not be added: {', '.join(rejected_toppings)}")

        created_pizza = order_service.get_pizza(pizza_name)
        messagebox.showinfo("Pizza Created", f"You have ordered: {created_pizza} for €{created_pizza.calc_price()}")
        pizza_window.destroy()

    tk.Button(frame, text="Confirm", command=confirm).grid(row=5, column=0, columnspan=2, pady=10)


def add_pizza():
    create_pizza()


def finish_order():
    messagebox.showinfo("Order Summary", str(order_service.get_order()))
    root.quit()


order_service = OrderService()

root = tk.Tk()
root.title("Pizza Ordering System")
root.geometry("300x150")

tk.Button(root, text="Add Pizza", command=add_pizza, width=20).pack(pady=5)
tk.Button(root, text="Finish Order", command=finish_order, width=20).pack(pady=5)

root.mainloop()