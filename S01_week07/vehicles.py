class Vehicle:
    def __init__(self, make, colour, num_seats=5):
        self.make = make
        self.colour = colour
        self.num_seats = num_seats

    def __eq__(self, other):
        if not isinstance(other, Vehicle):
            return NotImplemented

        if self.make != other.make:
            return False
        if self.colour != other.colour:
            return False
        if self.num_seats != other.num_seats:
            return False

        return True
