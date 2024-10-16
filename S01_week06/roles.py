import datetime as dt


class Person:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

    def calc_age(self):
        today = dt.datetime.now()
        num_days = (today - self.dob).days
        return int((num_days / 365))

    def display(self):
        print(f"{self.name} was born on {self.dob}.")
