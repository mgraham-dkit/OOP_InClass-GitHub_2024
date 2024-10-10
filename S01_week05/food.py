class Item:
    def __init__(self, name, desc="To be added later."):
        self.name = name
        self.desc = desc

    def __str__(self):
        return f"{self.name}: {self.desc}"


class Pizza(Item):
    # Shared information - one copy shared by all Pizza instances
    # Reference these using Pizza.variable_name
    size_options = {
        "small": 10,
        "medium": 12,
        "large": 15,
        "extra large": 18
    }

    topping_options = ["pineapple", "mozzarella", "brie", "goat cheese", "tomato", "pepperoni", "ham", "mushroom",
                       "chicken", "peppers", "onions", "meatballs", "bbq sauce", "tomato sauce"]
    max_topping_count = 10
    topping_price = 0.85

    # Constructor - deals with information for a specific Pizza instance
    def __init__(self, pizza_name, pizza_desc="Custom pizza", size="medium", toppings=None):
        super().__init__(pizza_name, pizza_desc)
        # As there are only a specific set of allowable sizes,
        # confirm that the supplied one is allowable before using it
        # If it's not valid, use a default value
        if not Pizza.validate_size(size):
            size = "medium"
        self._size = size.lower()

        # If no toppings were supplied, create an empty list
        # to hold any potential toppings added in future
        if toppings is None:
            toppings = []
        self._toppings = toppings

    @staticmethod
    def validate_size(size):
        if size.lower() in Pizza.size_options:
            return True
        else:
            return False

    def set_size(self, size):
        if Pizza.validate_size(size):
            self._size = size

    def get_size(self):
        return self._size

    def get_num_toppings(self):
        return len(self._toppings)

    def add_topping(self, topping):
        if self.get_num_toppings() < Pizza.max_topping_count and topping.lower() in Pizza.topping_options:
            self._toppings.append(topping)
            return True
        else:
            return False

    def calc_price(self):
        base_price = Pizza.size_options[self._size]
        toppings_price = self.get_num_toppings() * Pizza.topping_price
        return base_price + toppings_price

    def __str__(self):
        if not self._toppings:
            toppings = "no toppings."
        else:
            toppings = self._toppings[0]
            for i in range(1, len(self._toppings)):
                toppings += f", {self._toppings[i]}"

        return super().__str__() + "\n" + f"{self._size.capitalize()} pizza with {toppings}"


class Order:
    def __init__(self, items=None):
        if items is None:
            items = {}

        self.items = items

    def calc_price(self):
        total = 0
        for order in self.items.values():
            total += order.calc_price()

        return total

    def add_item(self, item):
        # Check if there is an item to be added
        # Check that the item name isn't already used
        if item is None or item.name.lower() in self.items:
            return False

        # Add the new item to the dictionary with its name as the key
        self.items[item.name.lower()] = item
        return True

    def remove_item(self, item):
        # Check that item to be removed exists
        if item is None:
            return False

        # Check that item is not in dictionary
        if item.name.lower() not in self.items:
            return False

        # Remove item from dictionary
        del self.items[item.name.lower()]
        return True

    def __str__(self):
        return "Items: \n" + "\n".join(str(item) for item in self.items.values())
