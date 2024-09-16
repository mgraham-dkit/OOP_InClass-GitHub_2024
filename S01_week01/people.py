class Person:
    first_name = "Joe"
    second_name = "Bloggs"
    age = 21
    left_handed = False

    def display(self):
        print(f"{self.first_name} {self.second_name} is {self.age} years old. Their lefthanded status is {self.left_handed}")