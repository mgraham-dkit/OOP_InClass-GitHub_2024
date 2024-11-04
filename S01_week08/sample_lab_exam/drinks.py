from __future__ import annotations

class Drink:
    def __init__(self, drink_name: str, customer_name: str, price: float) -> None:
        self.drink_name = drink_name
        self.customer_name = customer_name
        self.price = price

    def calculate_price(self) -> float:
        return self.price

    def __eq__(self, other: Drink) -> bool:
        if not isinstance(other, Drink):
            return False

        if self.price != other.price:
            return False
        if self.drink_name != other.drink_name:
            return False
        if self.customer_name != other.customer_name:
            return False

        return True

    def __ne__(self, other: Drink) -> bool:
        return not self == other

    def __str__(self) -> str:
        return f"{self.drink_name} ordered by {self.customer_name} for €{self.price}"

    def __repr__(self) -> str:
        return f"Drink[drink_name={self.drink_name}, customer_name={self.customer_name}, price={self.price}"