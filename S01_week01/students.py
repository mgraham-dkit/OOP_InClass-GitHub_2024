class Student:
    id = "D000"
    name = "Michelle"
    module = "OO Programming"


if __name__ == "__main__":
    person1 = Student()
    person1.id = "D000123"
    person1.name = "Henry Higgins"
    person1.module = "Automation"

    person2 = Student()

    # Create a list from the two objects
    people = [person1, person2]
    for person in people:
        print(f"Person name: {person.name}")
