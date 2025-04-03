from __future__ import annotations


class Item:
    def __init__(self, name: str, desc: str ="To be added later."):
        self.name = name
        self.desc = desc

    def __str__(self) -> str:
        return f"{self.name}: {self.desc}"

    def __eq__(self, other: Item) -> bool | NotImplemented:
        if not isinstance(other, Item):
            return NotImplemented

        if self.name != other.name:
            return False
        if self.desc.lower() != other.desc.lower():
            return False

        return True

    def __ne__(self, other: Item) -> bool | NotImplemented :
        return not self == other

    def __repr__(self) -> str:
        return f"Item[name={self.name}, desc={self.desc}]"

    def __lt__(self, other: Item) -> bool | NotImplemented :
        if not isinstance(other, Item):
            return NotImplemented

        return self.name < other.name

    def __le__(self, other: Item) -> bool | NotImplemented:
        if not isinstance(other, Item):
            return NotImplemented

        return self.name <= other.name

    def __gt__(self, other: Item) -> bool | NotImplemented:
        if not isinstance(other, Item):
            return NotImplemented

        return self.name > other.name

    def __ge__(self, other: Item) -> bool | NotImplemented:
        if not isinstance(other, Item):
            return NotImplemented

        return self.name >= other.name


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

    def get_toppings(self):
        return list(self._toppings)

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
            toppings = ", ".join(self._toppings)
            # toppings = self._toppings[0]
            # for i in range(1, len(self._toppings)):
            #     toppings += f", {self._toppings[i]}"

        return super().__str__() + "\n" + f"{self._size.capitalize()} pizza with {toppings}"

    def __lt__(self, other):
        if not isinstance(other, Pizza):
            return NotImplemented

        if self._size == other._size:
            return len(self._toppings) < len(other._toppings)

        return self._size < other._size

    def __le__(self, other):
        if not isinstance(other, Pizza):
            return NotImplemented

        if self._size == other._size:
            return len(self._toppings) < len(other._toppings)

        return self._size < other._size

    def __add__(self, other) -> NotImplemented | Pizza:
        if not isinstance(other, Pizza):
            return NotImplemented

        if self._size == other._size:
            new_size = self._size
        else:
            new_size = Pizza.size_options[2]

        new_toppings = list(self._toppings)
        new_toppings.extend(other._toppings)

        new_name = self.name + " combined with " + other.name
        new_desc = self.desc + ". Added to : " + other.desc

        return Pizza(new_name, new_desc, new_size, new_toppings)


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

    def get_item(self, item_name):
        return self.items.get(item_name.lower())

    def __str__(self):
        return "Items: \n" + "\n".join(str(item) for item in self.items.values())



if __name__ == "__main__":
    pizzaA = Pizza("Michelle's pizza", "Yummy", "medium", ['pepperoni','brie'])
    pizzaB = Pizza("My pizza", "Tasty", "medium", ["pineapple", "chicken"])

    print(pizzaA)
    print(pizzaB)
