from food import Pizza
from services import OrderService


def get_int(display_text: str) -> int:
    valid = False
    while not valid:
        try:
            num = int(input(display_text))
            valid = True
        except ValueError as e:
            print("Integer required.")

    return num


def choose_topping():
    print("Available toppings:")
    for i, topping in enumerate(Pizza.topping_options):
        print(f"{i+1}: {topping.capitalize()}")

    print("Enter -1 to exit without adding another topping")

    valid = False
    topping_choice = -1
    while not valid:
        topping_choice = get_int("Please enter your selection: ")
        if 0 < topping_choice <= len(Pizza.topping_options) or topping_choice == -1:
            valid = True
        else:
            print(f"Please enter a valid option from the toppings menu! (from 1 to {len(Pizza.topping_options)}")

    if topping_choice != -1:
        return Pizza.topping_options[topping_choice-1]
    else:
        return None


def choose_size():
    print("Available sizes:")
    for size in Pizza.size_options:
        print(f"- {size.capitalize()}")

    valid = False
    while not valid:
        choice = input("Please enter your selection: ")
        if choice.lower() in Pizza.size_options:
            valid = True
        else:
            print(f"Please enter a valid size.")

    return choice


def get_toppings():
    toppings = []
    finished_toppings = False
    while not finished_toppings:
        choice = input("Do you wish to add a new topping to your item? (Y for yes, any other key for no):> ")
        if choice.upper() == "Y":
            new_topping = choose_topping()
            if new_topping is not None:
                print(f"{new_topping.capitalize()} added!")
                toppings.append(new_topping)
        else:
            finished_toppings = True

    return toppings


def create_pizza():
    pizza_name = input("Please enter your item's name: ")
    size = choose_size()
    toppings = get_toppings()
    rejected_toppings = order_service.add_pizza(pizza_name, pizza_size=size, pizza_toppings=toppings)
    if rejected_toppings:
        print("The following toppings could not be added:")
        for i, rejected in enumerate(rejected_toppings):
            print(f"{i+1}: {rejected}")

    return pizza_name

order_service = OrderService()

finished = False
while not finished:
    pizza_name = create_pizza()
    print("Pizza complete!")
    created_pizza = order_service.get_pizza(pizza_name)
    print(f"You have ordered: {created_pizza} for €{created_pizza.calc_price()}")
    choice = input("Do you wish to add another pizza to your order? (Y for yes, any other key for no):> ")
    if choice.upper() != "Y":
        finished = True

#print(order_service.get_order())
