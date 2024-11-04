import datetime as dt
from __future__ import annotations


class Person:
    def __init__(self, name: str, dob: dt.datetime) -> None:
        self.name = name
        self.dob = dob

    def calc_age(self) -> int:
        today = dt.datetime.now()
        num_days = (today - self.dob).days
        return int((num_days / 365))

    def display(self) -> None:
        print(f"{self.name} was born on {self.dob}.")

    def __eq__(self, other: Person) -> bool | NotImplemented:
        if not isinstance(other, Person):
            return False

        if self.name != other.name:
            return False
        if self.dob != other.dob:
            return False

        return True

    def __ne__(self, other: Person) -> bool | NotImplemented:
        return not self == other

    def __format__(self, format_spec):
        match format_spec.lower():
            case "simple":
                return f"{self.name}, born {self.dob.strftime("%d-%m-%Y")}"
            case "file":
                return f"{self.name}%%{self.dob.strftime("%d-%m-%Y")}"
            case _:
                return self.__str__()


class Student(Person):
    _courses: list[str] = ["computing systems and operations", "computing", "software development", "business", "irish history", "data science"]
    _student_count: int = 0

    # Type hinting on method signature
    # -> States what the method will return
    # : States what type the variable contains
    def __init__(self, name: str, dob: dt.datetime, course: str = None, year: int = 1) -> None:
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

    @staticmethod
    def validate_course(course_name: str) -> bool:
        if course_name is None or course_name.lower() not in Student._courses:
            return False
        return True

    @staticmethod
    def get_valid_courses() -> list[str]:
        valid_courses = Student._courses.copy()
        return valid_courses

    # As specified, this one is a class method, not just a static method
    @classmethod
    def add_course(cls, course_name: str) -> bool:
        course_name = course_name.lower()
        if course_name not in cls._courses:
            cls._courses.append(course_name)
            return True

        return False

    def display(self) -> None:
        super().display()
        print(f"ID: {self.student_id}, in year {self.year} of {self._course}")

    def __eq__(self, other) -> bool | NotImplemented:
        if not isinstance(other, Student):
            return NotImplemented

        if not super().__eq__(other):
            return False

        if self.student_id != other.student_id:
            return False
        if self._course != other._course:
            return False
        if self.year != other.year:
            return False

        return True

    def __ne__(self, other) -> bool | NotImplemented:
        return not self == other
