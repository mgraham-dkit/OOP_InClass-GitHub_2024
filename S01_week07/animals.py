import datetime as dt


class Animal:
    def __init__(self, dob, weight, name="Critter"):
        self.dob = dob
        self.weight = weight
        self.name = name

    def calc_age(self):
        today = dt.datetime.now()
        num_days = (today - self.dob).days
        return int((num_days / 365))

    def display(self):
        print(f"{self.name} was born on {self.dob}, weighing {self.weight}.")

    def __eq__(self, other):
        if not isinstance(other, Animal):
            return NotImplemented

        if self.dob != other.dob:
            return False
        if self.weight != other.weight:
            return False
        if self.name != other.name:
            return False

        return True

    def __ne__(self, other):
        return not self == other


class Dog(Animal):
    def __init__(self, dob, weight, breed, name="Bingo", personality="friendly"):
        super().__init__(dob, weight, name)
        self.breed = breed
        self.personality = personality

    def display(self):
        super().display()
        print(f"\tIts breed is {self.breed}, with major {self.personality} personality.")

    def __eq__(self, other):
        if not isinstance(other, Dog):
            return NotImplemented

        if not super().__eq__(self, other):
            return False

        if self.breed != other.breed:
            return False
        if self.personality != other.personality:
            return False

        return True

    def __ne__(self, other):
        return not self == other
