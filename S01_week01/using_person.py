from people import Person

def create_person():
    first_name = input("Please enter first name: ")
    last_name = input("Please enter last name: ")
    age = int(input("Please enter your age: "))
    handed = input("Are you left-handed? (Y for yes, any other key for no.) ")

    p = Person()
    p.first_name = first_name
    p.second_name = last_name
    p.age = age
    if handed.upper() == "Y":
        p.left_handed = True
    else:
        p.left_handed = False

    return p


# Creating a Person object
p1 = Person()
name = p1.first_name + " " + p1.second_name
if p1.left_handed is False:
    name = name.upper()
else:
    p1.left_handed = False

print(name)

people = []
for i in range(2):
    p = create_person()
    people.append(p)

# Print the first name of each person in thepeople list:
i = 0
for person in people:
    person.display()