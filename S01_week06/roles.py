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


class Student(Person):
    # This should be a static list of valid course names and should be private.
    # Private is achieved by using _ on the variable name
    # This is a static variable because it's been made outside all methods and is not referenced with self.
    _courses = ["computing systems and operations", "computing", "software development", "business", "irish history", "data science"]
    # This is static so that it will be shared over all Students (NOT all Persons!)
    _student_count = 0

    # Name and dob are required because there are no values provided for them here
    # Course is set to None so it can be set to the list content in the __init__
    def __init__(self, name, dob, course=None, year=1):
        # Pass the Person-related information to the Person constructor so it can handle storing those values
        super().__init__(name, dob)

        # Check if the supplied course name is valid
        if not Student.validate_course(course):
            # If it's not valid, set it to the first valid course.
            course = Student._courses[0]
        self._course = course

        # Increase the count of students created in the system - this will run in every constructor,
        # i.e. every time a new Student is made
        Student._student_count += 1
        self.student_id = Student._student_count

        # Check the course year is less than or equal to 0 - reset it to 1 if it is
        if year < 1:
            year = 1
        self.year = year

    # To clean up our validation, we can write a separate method to check if a supplied course name is allowable
    # This is a static method as it's not operating on any of the object's information
    @staticmethod
    def validate_course(course_name):
        # Check if the name is none before we do anything - this avoids crashing on the lower() call
        # Use lower() to make sure we don't need to consider case in the comparison
        # If the name isn't in the allowable list, return false
        if course_name is None or course_name.lower() not in Student._courses:
            return False

        # If it passes the above checks, return true because the name is valid
        return True

    # As specified, this one is defined explicitly as just a static method, not a class method
    @staticmethod
    # Create a static method to get the list of valid courses
    def get_valid_courses():
        # We don't give back the actual list of valid courses
        # as we don't want to let others have a way to change the list directly
        # Make a copy so that any changes they make would not impact the list here
        valid_courses = Student._courses.copy()
        return valid_courses

    # As specified, this one is a class method, not just a static method
    @classmethod
    def add_course(cls, course_name):
        # Convert the name to lowercase to match the other courses in the list
        course_name = course_name.lower()
        # If the supplied course is not in the list, add it and return True
        if course_name not in cls._courses:
            cls._courses.append(course_name)
            return True

        # Otherwise return false
        return False

    def display(self):
        super().display()
        print(f"ID: {self.student_id}, in year {self.year} of {self._course}")
