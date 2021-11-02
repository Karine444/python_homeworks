import json
import requests
import datetime


with open ("img_links.json") as f:
    data = json.load(f)

def img_download(name):
    for url in data:
        if url['img_name'] == name:
            img_url = url['img_url']
            img_name = url['img_name']
            try:
                response = requests.get(img_url)
                with open(img_name, 'wb') as photo:
                    photo.write(response.content)
            except KeyError:
                print('There is a connection error')


try:
    with open("download_history.json", 'x') as fd:
        json.dump([], fd, indent=4)
except FileExistsError as err:
    print("file already exists: passing")


class MyJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return o.to_json()
        else:
            super().default(o)

def insert_user_to_json(img_history):

    with open("download_history.json", 'r') as json_file:
            history = json.load(json_file)

    history.append(img_history)
    with open('download_history.json', 'w') as json_file:
        json.dump(history, json_file, indent=4, cls=MyJSONEncoder)


while True:
    img_d = input('What picture do you want to download?\n\t')
    img_download(f"{img_d}.jpg")
    insert_user_to_json(f'{img_d}.jpg was downloaded on {datetime.datetime.now()}')
    again = input('Do you want to download another image? yes/no\n\t')
    if again == 'yes':
        continue
    else:
        print("Thank you for choosing us ☺ GoodBye!")
        break

