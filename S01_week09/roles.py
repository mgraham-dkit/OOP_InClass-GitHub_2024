from __future__ import annotations


class User:
    def __init__(self, _username: str, _password: str):
        if _username is None or len(_username) == 0:
            print(f"Username \"{_username}\" cannot be empty/blank")
        self._username = _username

        if _password is None or len(_password) < 8:
            print(f"Password is too short.")

        if not User.validate_password(_password):
            print("Password did not fulfil requirements.")

        self._password = _password

    def check_credentials(self, username: str, password: str) -> bool:
        return self._username == username and self._password == password

    def change_password(self, username: str, old_pass: str, new_pass:str) -> bool:
        if not self.check_credentials(username, old_pass):
            return False

        if not User.validate_password(new_pass):
            return False

        self._password = new_pass
        return True

    @staticmethod
    def validate_password(password:str) -> bool:
        if len(password) < 8:
            return False

        # if not any(x.isupper() for x in password):
        #     return False
        # if not any(x.islower() for x in password):
        #     return False
        # if not any(x.isdigit() for x in password):
        #   return False
        # return True

        has_digit = False
        has_upper = False
        has_lower = False
        for char in password:
            if char.isupper():
                has_upper = True
            if char.islower():
                has_lower = True
            if char.isdigit():
                has_digit = True

            if has_digit and has_lower and has_upper:
                return True

        return False

    def __eq__(self, other: User) -> bool:
        if not isinstance(other, User):
            return NotImplemented

        if not self._username == other._username:
            return False
        return True

    def __ne__(self, other: User) -> bool:
        return not self == other

    def __repr__(self) -> str:
        temp_password = "*" * 8
        return f"User[_username={self._username}, _password={temp_password}]"

    def __str__(self) -> str:
        return f"Username: {self._username}"

    def __format__(self, format_spec: str) -> str:
        match format_spec.lower():
            case "short":
                return f"{self._username}"
            case "complete":
                temp_password = "*" * 8
                return f"{self._username}, password: {temp_password}"
            case _:
                return self.__str__()

    def __hash__(self) -> int:
        return hash(self._username)


class Moderator(User):
    def __init__(self, user: str, password: str, groups: list[str] | None = None):
        super().__init__(user, password)

        if groups is None:
            groups = []

        for i in range(len(groups)):
            groups[i] = groups[i].lower()

        self._modded_groups = groups

    def add_group(self, group: str) -> bool:
        group = group.lower()
        if group not in self._modded_groups:
            self._modded_groups.append(group)
            return True

        return False

    def get_groups(self) -> list[str]:
        groups = []
        for group in self._modded_groups:
            groups.append(group)

        return groups

    def __eq__(self, other: Moderator) -> bool:
        if not super().__eq__(other):
            return False
        if not isinstance(other, Moderator):
            return NotImplemented

        if not self._modded_groups == other._modded_groups:
            return False
        return True

    def __ne__(self, other: Moderator) -> bool:
        return not self == other

    def __repr__(self) -> str:
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
