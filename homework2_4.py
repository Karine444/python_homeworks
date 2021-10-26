import json

class User:
    def __init__(self, name, surname, email, phone_number):
        self.name = self.string_validation(name)
        self.surname = self.string_validation(surname)
        self.email = self.email_validator(email)
        self.phone_number = self.number_validation(phone_number)

    @staticmethod
    def string_validation(value):
        if value.isdigit():
            raise ValueError("Wrong Value")
        else:
            return value

    @staticmethod
    def number_validation(value):
        if type(value) == str:
            raise ValueError("Wrong Value")
        else:
            return value

    @staticmethod
    def email_validator(self, email):
        if "@" not in email:
            raise ValueError("Wrong type of email!!")
        return email

    def __str__(self):
        return f"{self.name} {self.surname} {self.email} {self.phone_number}"

    def __enter__(self):
        return self.__str__()

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def to_dict(self):
        return{"name":self.name, "surname":self.surname, "email":self.email, "phone_number":self.phone_number}


user_1 = User('Karine', 'Vardanyan', 'karine.vardanyan.444@mail.ru', '094758489')
user_2 = User('Anna', 'Simonyan', 'anna.simonyan.444@mail.ru', '098452515')
