from food import Pizza
from food import Order

def choose_topping():
    print("Available toppings:")
    for i, topping in enumerate(Pizza.topping_options):
        print(f"{i+1}: {topping.capitalize()}")

    print("Enter -1 to exit without adding another topping")

    valid = False
    choice = -1
    while not valid:
        choice = int(input("Please enter your selection: "))
        if 0 < choice <= len(Pizza.topping_options) or choice == -1:
            valid = True
        else:
            print(f"Please enter a valid option from the toppings menu! (from 1 to {len(Pizza.topping_options)}")

    if choice != -1:
        return Pizza.topping_options[choice-1]
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
    finished = False
    while not finished:
        choice = input("Do you wish to add a new topping to your pizza? (Y for yes, any other key for no):> ")
        if choice.upper() == "Y":
            new_topping = choose_topping()
            if new_topping is not None:
                print(f"{new_topping.capitalize()} added!")
                toppings.append(new_topping)
        else:
            finished = True

    return toppings


def create_pizza():
    size = choose_size()
    toppings = get_toppings()
    return Pizza(size, toppings)


new_pizza = create_pizza()
print("Pizza complete!")
print(f"You have ordered: {new_pizza} for €{new_pizza.calc_price()}")

