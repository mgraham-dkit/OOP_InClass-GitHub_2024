class Product:
    def __init__(self, prod_id: str, prod_name: str, cost: float, retail: float, quantity: int = 10):
        if not prod_name:
            raise ValueError(f"Name must be supplied for Product")
        self.prod_name = prod_name

        if cost < 0 or retail < 0:
            raise ValueError(f"All prices must be greater than 0.")
        self.cost = cost
        self.retail = retail

        if quantity < 0:
            raise ValueError("Quantity cannot be a negative value.")
        self.quantity = quantity

        verdict, err_msg = Product.validate_id(prod_id)
        if not verdict:
            raise ValueError(f"Invalid product ID supplied - {err_msg}")
        self.prod_id = prod_id.upper()

    @staticmethod
    def validate_id(prod_id: str) -> tuple[bool, str|None]:
        if not prod_id:
            return False, "No product ID supplied"
        prod_id = prod_id.upper()

        if len(prod_id) < 3:
            return False, "Product ID is too short"

        if not prod_id.startswith("ID"):
            return False, "Malformed product ID - ID must begin with \"ID\""

        return True, None



class Book(Product):
    def __init__(self, prod_id: str, prod_name: str, cost: float, retail: float, quantity: int, author: str, genres:list[str] = None):
        super().__init__(prod_id, prod_name, cost, retail, quantity)

        self.author = author

        if genres is None:
            genres = ["fiction"]

        self._genres = []
        for genre in genres:
            self._genres.append(genre.lower())

        # self._genres = [genre.lower() for genre in genres]