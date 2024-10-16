import datetime as dt
import random as rand

from animals import Animal
from animals import Dog


def as_date(text_date):
    date_format = "%d/%m/%Y"
    return dt.datetime.strptime(text_date, date_format)


def create_animal(date, weight, name):
    dob = as_date(date)
    a = Animal(dob, weight, name)
    return a


def create_dog(date, weight, name, breed, personality):
    dob = as_date(date)
    dog = Dog(dob, weight, breed, name, personality)
    return dog


def create_user_creature(animal_type):
    dob = input("Please enter date of birth (format: DD/MM/YYYY): ")
    weight = float(input("Please enter weight: "))
    name = input("Please enter name: ")
    if animal_type.upper() == "DOG":
        breed = input("Please enter the breed: ")
        personality = input("What sort of personality does the dog have? : ")
        return create_dog(dob, weight, name, breed, personality)
    else:
        return create_animal(dob, weight, name)


animals = []
a1 = create_animal("12/04/2013", 10, "Chico")
animals.append(a1)

a2 = create_animal("15/12/2022", 4, "Blinky")
animals.append(a2)

a3 = create_animal("22/07/2019", 100, "Nellie")
animals.append(a3)

for i in range(2):
    user_animal = create_user_creature("ANIMAL")
    animals.append(user_animal)

d1 = create_dog("27/03/2013", 19, "Skye", "Cockapoo", "Gentle")
animals.append(d1)

d2 = create_dog("04/10/2010", 29, "Rubble", "English Bulldog", "Hungry")
animals.append(d2)

rand.shuffle(animals)

print("Animals in the menagerie:")
for a in animals:
    a.display()
print()

print("Animals aged 2 and under:")
for a in animals:
    if a.calc_age() <= 2:
        a.display()
