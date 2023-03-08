class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username: str):
        if 5 <= len(username) <= 15:
            self.__username = username
        else:
            raise ValueError("The username must be between 5 and 15 characters.")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password: str):
        if len(password) >= 8:
            upper_case_letters = [x for x in password if x.isupper()]
            digits = [x for x in password if x.isdigit()]
            if len(upper_case_letters) >= 1 and len(digits) >= 1:
                self.__password = password
            else:
                raise ValueError(
                    "The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        else:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'


