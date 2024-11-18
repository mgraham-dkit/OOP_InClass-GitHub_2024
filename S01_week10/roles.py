# As we want to type-hint objects of the same type as the classes in this file
# we need to import the annotations module to change when the type hints will be processed
from __future__ import annotations


class User:
    # Define a constructor that takes in a username and password
    def __init__(self, _username: str, _password: str):
        # Validate and inform if the data is "bad"
        if _username is None or len(_username) == 0:
            print(f"Username \"{_username}\" cannot be empty/blank")
        # Save the username to this User
        self._username = _username

        # Validate and inform if the data is "bad"
        if _password is None or len(_password) < 8:
            print(f"Password is too short.")

        # Validate and inform if the data is "bad"
        if not User.validate_password(_password):
            print("Password did not fulfil requirements.")

        # Save the password to this User
        self._password = _password

    def check_credentials(self, username: str, password: str) -> bool:
        # Confirm username and password match stored values
        return self._username == username and self._password == password

    def change_password(self, username: str, old_pass: str, new_pass: str) -> bool:
        # Check the credentials are correct - if not then we shouldn't save the new password
        # as the user doesn't have the right permissions
        if not self.check_credentials(username, old_pass):
            return False

        # Check the new password meets the requirements - if not then don't change it
        if not User.validate_password(new_pass):
            return False

        # User has proven themselves and new password is acceptable - change it and return True
        self._password = new_pass
        return True

    @staticmethod
    def validate_password(password:str) -> bool:
        # Length check first as it's the "cheapest"
        if len(password) < 8:
            return False

        # Alternative approach using list comprehensions
        # Each if checks a specific requirement

        # Check if there's an uppercase
        # if not any(x.isupper() for x in password):
        #     return False

        # Check if there's a lowercase
        # if not any(x.islower() for x in password):
        #     return False

        # Check if there's a letter
        # if not any(x.isdigit() for x in password):
        #   return False

        # All checks have passed, so return True.
        # return True

        has_digit = False
        has_upper = False
        has_lower = False
        # For each character in the password, check if it's an upper, a lower or a number
        # Update appropriate flag accordingly
        for char in password:
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char.isdigit():
                has_digit = True

            # If all flags have been set to True, all requirements are met
            if has_digit and has_lower and has_upper:
                return True

        # If we get through all characters in the string and get to here, one or more requirements weren't met
        return False

    def __eq__(self, other: User) -> bool:
        # If it's not a User, return NotImplemented
        if not isinstance(other, User):
            return NotImplemented

        # If the usernames don't match, return false
        if not self._username == other._username:
            return False
        return True

    def __ne__(self, other: User) -> bool:
        return not self == other

    def __repr__(self) -> str:
        # Create a piece of text to represent the password (don't include the real password)
        temp_password = "*" * 8
        return f"User[_username={self._username}, _password={temp_password}]"

    def __str__(self) -> str:
        return f"Username: {self._username}"

    def __format__(self, format_spec: str) -> str:
        match format_spec.lower():
            case "short":
                return f"{self._username}"
            case "complete":
                # Create a piece of text to represent the password (don't include the real password)
                temp_password = "*" * 8
                return f"{self._username}, password: {temp_password}"
            case _:
                return self.__str__()

    def __hash__(self) -> int:
        # Username is unique and will not change, so this is a safe value to use as the basis of __hash__()
        return hash(self._username)

    def __gt__(self, other: User) -> bool | NotImplemented:
        if not isinstance(other, User):
            return NotImplemented

        if self._username > other._username:
            return True
        else:
            return False

    def __ge__(self, other: User) -> bool | NotImplemented:
        if not isinstance(other, User):
            return NotImplemented

        if self._username >= other._username:
            return True
        else:
            return False

    def __lt__(self, other: User) -> bool | NotImplemented:
        if not isinstance(other, User):
            return NotImplemented

        return self._username < other._username

    def __le__(self, other: User) -> bool | NotImplemented:
        if not isinstance(other, User):
            return NotImplemented

        return self._username <= other._username


# Define a class that extends the User class (creates a more specific version of a User)
class Moderator(User):
    # Define a constructor to create a Moderator
    def __init__(self, user: str, password: str, groups: list[str] | None = None):
        # Get the User class to set up the parts of the Moderator that belong to User
        super().__init__(user, password)

        # Handle where groups list wasn't passed in
        if groups is None:
            groups = []

        # Convert all group data to lowercase (to prevent case-sensitivity later)
        for i in range(len(groups)):
            groups[i] = groups[i].lower()

        # Store the groups in this Moderator
        self._modded_groups = groups

    def add_group(self, group: str) -> bool:
        # Convert to lowercase to avoid case-sensitivity issues
        group = group.lower()
        # If the new group isn't already there, add it
        if group not in self._modded_groups:
            self._modded_groups.append(group)
            return True

        return False

    def get_groups(self) -> list[str]:
        # Create a new list to store all groups from this Moderator
        groups = []
        # Fill it with all this Moderator's groups (this guarantees the list the Moderator owns remains private)
        for group in self._modded_groups:
            groups.append(group)

        return groups

    def __eq__(self, other: Moderator) -> bool:
        # If the user parts don't match, the other object doesn't equal this one
        if not super().__eq__(other):
            return False
        # If it's not a moderator, the other object doesn't equal this one
        if not isinstance(other, Moderator):
            return NotImplemented

        # If the groups list doesn't match this moderator's, the objects aren't equal
        if not self._modded_groups == other._modded_groups:
            return False
        return True

    def __ne__(self, other: Moderator) -> bool:
        return not self == other

    def __repr__(self) -> str:
        # Create a piece of text to display instead of the real password
        temp_password = "*" * 8
        return f"Moderator[_username={self._username}, _password={temp_password}, _modded_groups={self._modded_groups}]"

    def __str__(self) -> str:
        return f"Username: {self._username}. Modded groups: {self._modded_groups}"

    def __format__(self, format_spec: str) -> str:
        match format_spec.lower():
            case "short":
                return f"{self._username} mods {len(self._modded_groups)} groups."
            case "complete":
                temp_password = "*" * 8
                return f"{self._username}, password: {temp_password}, _modded_groups={self._modded_groups}"
            case _:
                return self.__str__()
