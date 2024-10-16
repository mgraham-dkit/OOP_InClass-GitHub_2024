import datetime as dt
import random as rand


from roles import Person
from roles import Student


def as_date(text_date):
    date_format = "%d/%m/%Y"
    return dt.datetime.strptime(text_date, date_format)


# Helper function : fills the list with hard-coded objects
# This just cleans the code for the main program up a bit!
def bootstrap_list():
    people_list = []
    # Create Person objects and add to list
    p1 = Person("Helen Troy", "12/04/2013")
    p2 = Person("Miranda Bailey", "15/12/2022")
    p3 = Person("Ben Warren", "22/07/2019")
    # Add multiple elements at once!!
    people_list.extend([p1, p2, p3])

    # Create Student objects and add to list
    valid_courses = Student.get_valid_courses()
    s1 = Student("Jackson Avery", "12/11/1970", valid_courses[0], 3)
    s2 = Student("Catherine Fox", "05/03/1947", valid_courses[1], 2)
    s3 = Student("April Kepner", "02/01/1973", valid_courses[0], 3)
    # Add multiple elements at once!!
    people_list.extend([s1, s2, s3])

    return people_list


# Helper function - this deals with making sure the course used is always a valid one
def get_valid_course():
    course = None
    # Get the list of valid courses so we can show it to the user
    # Get it outside the loop so we don't make a new list every time
    valid_courses = Student.get_valid_courses()

    # Loop to repeatedly take in a course name until they enter a valid one
    valid = False
    while not valid:
        print(f"Available valid courses: {valid_courses}")
        course = input("Please enter the course name: ")
        # If the course is valid (based on the logic of the Student class) then stop the loop
        if Student.validate_course(course):
            valid = True
        else:
            print("Please enter a VALID course.")

    return course


# Helper function - this deals with making sure the year used is always a valid one
def get_valid_year():
    year = -1

    # Loop to repeatedly take in a year until they enter a valid one (more than 0)
    valid = False
    while not valid:
        year = int(input("Please enter the student's year: "))
        # If the year is valid (greater than 0)
        if year > 0:
            valid = True
        else:
            print("The student's course year cannot be <= 0.")

    return year


# Helper function - This creates the appropriate type of object based on the role name supplied
def create_role(role):
    name = input("Please enter name: ")
    dob = input("Please enter date of birth (format: DD/MM/YYYY): ")
    if role.upper() == "STUDENT":
        course = get_valid_course()
        year = get_valid_year()
        return Student(name, dob, course, year)
    else:
        return Person(name, dob)


# Helper function - this displays the menu of role options
def display_menu():
    print("1) Create a new Person role.")
    print("2) Create a new Student role.")


# Helper function - this takes in the type of object to be created
def get_role_choice():
    role = None
    valid = False
    while not valid:
        display_menu()
        choice = input("Enter your choice: ")
        match choice:
            case "1":
                role = "PERSON"
                valid = True
            case "2":
                role = "STUDENT"
                valid = True
            case _:
                print("Not a valid option.")

    return role


# Helper function - this manages repeatedly creating new input-based objects
def get_user_input(people_list):
    choice = input("Do you want to create a new role? (Y/y to create, any other key to stop)")
    while choice.upper() == "Y":
        role = get_role_choice()
        created = create_role(role)
        people_list.append(created)
        choice = input("Do you want to create another role? (Y/y to create, any other key to stop)")


people = bootstrap_list()
get_user_input(people)
rand.shuffle(people)

print("People in the college:")
for p in people:
    p.display()
print()

print(f"Number of students in the system: {Student._student_count}")

# This can also be achieved by actually counting student objects:
student_total = 0
for person in people:
    # If the current object is an instance of the Student class, increase counter
    if isinstance(person, Student):
        student_total += 1

print(f"Total number of student objects encountered: {student_total}")
