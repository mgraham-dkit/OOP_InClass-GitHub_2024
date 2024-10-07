class Pizza:
    size_options = {
        "small": 10,
        "medium": 12,
        "large": 15,
        "extra large": 18
    }

    topping_options = ["pineapple", "mozzarella", "brie", "goat cheese", "tomato", "pepperoni", "ham", "mushroom", "chicken", "peppers", "onions", "meatballs", "bbq sauce", "tomato sauce"]
    max_topping_count = 10
    topping_price = 0.85

    def __init__(self, size="medium", toppings=None):
        if not Pizza.validate_size(size):
            size = "medium"
        self._size = size

        if toppings is None:
            toppings = []
        self._toppings = toppings

    def set_size(self, size):
        if Pizza.validate_size(size):
            self._size = size

    @staticmethod
    def validate_size(size):
        if size.lower() in Pizza.size_options:
            return True
        else:
            return False

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
        return f"{self._size} pizza with {self._toppings}"
