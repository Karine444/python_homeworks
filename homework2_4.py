import json
# import yaml

class User:
    def __init__(self, name, surname):
        self.name = self.string_validation(name)
        self.surname = self.string_validation(surname)

    @staticmethod
    def string_validation(value):
        if value.isdigit():
            raise ValueError("Wrong Value")
        else:
            return value

    def __str__(self):
        return f"{self.name} {self.surname}"

    def to_json(self):
        return{"name":self.name, "surname":self.surname}


class MyJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return o.to_json()
        else:
            super().default(o)

try:
    with open("users.json", 'x') as fd:
        json.dump([], fd, indent=4)
except FileExistsError as err:
    print("file already exists: passing")

if __name__ == "__main__":

    user_1 = User('Karine', 'Vardanyan')
    user_2 = User('Vardan', 'Simonyan')

    user_list = [user_1, user_2]


def insert_user_to_json(user_as_dict):

    with open("users.json", 'r') as json_file:
            users = json.load(json_file)

    users.append(user_as_dict)
    with open('users.json', 'w') as json_file:
        json.dump(users, json_file, indent=4, cls=MyJSONEncoder)



for user in user_list:
    insert_user_to_json(user)


