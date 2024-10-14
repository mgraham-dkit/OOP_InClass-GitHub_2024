import datetime as dt

from animals import Animal
from animals import Dog


def as_date(text_date):
    date_format = "%d/%m/%Y"
    return dt.datetime.strptime(text_date, date_format)


def create_animal(date, weight, name):
    dob = as_date(date)
    a = Animal(dob, weight, name)
    return a


animals = []
a1 = create_animal("12/04/2013", 10, "Chico")
animals.append(a1)

a2 = create_animal("15/12/2022", 4, "Blinky")
animals.append(a2)

a3 = create_animal("22/07/2019", 100, "Nellie")
animals.append(a3)

for a in animals:
    a.display()
