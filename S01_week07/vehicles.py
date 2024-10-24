from __future__ import annotations


class Vehicle:
    def __init__(self, make: str, colour: str, num_seats: int = 5) -> None:
        self.make = make
        self.colour = colour
        self.num_seats = num_seats

    def __eq__(self, other: Vehicle) -> bool:
        if not isinstance(other, Vehicle):
            return NotImplemented

        if self.make != other.make:
            return False
        if self.colour != other.colour:
            return False
        if self.num_seats != other.num_seats:
            return False

        return True

    def __repr__(self) -> str:
        return f"Vehicle[make={self.make}, colour={self.colour}, num_seats={self.num_seats}]"

    def __str__(self) -> str:
        return f"{self.make} vehicle in {self.colour} with {self.num_seats} seats"


class Bike(Vehicle):
    def __init__(self, make, colour, num_seats, num_gears=3):
        super().__init__(make, colour, num_seats)
        self.num_gears = num_gears

    def __eq__(self, other: Bike):
        if not isinstance(other, Bike):
            return NotImplemented

        if not super().__eq__(other):
            return False

        if self.num_gears != other.num_gears:
            return False

        return True

    def __repr__(self):
        return f"Bike[make={self.make}, colour={self.colour}, num_seats={self.num_seats}, num_gears={self.num_gears}]"

    def __str__(self):
        return f"{self.make} bike in {self.colour} with {self.num_seats} seats and {self.num_gears} gears."
