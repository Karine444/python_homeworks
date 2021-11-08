import sqlite3
from sqlite3 import Error
import os
import sys
from pprint import pprint
import json

database = os.path.join(os.getcwd(), "film_data.db")
print(database)
try:
    conn = sqlite3.connect(database)
except Error as e:
    print(e)
    sys.exit()

curs = conn.cursor()

select_title = """select title from film_data
            where title like "B%";
        """
result = curs.execute(select_title)
pprint(result.fetchall())


select_max = """SELECT title, MAX(length) 
            FROM film_data;"""

result_2 = curs.execute(select_max)
pprint(result_2.fetchall())



class create_dict(dict):

    def __init__(self):
        self = dict()

    def add(self, key, value):
        self[key] = value


dict = create_dict()
select_film_data = """SELECT * FROM film_data;"""
curs.execute(select_film_data)
result = curs.fetchall()

for row in result:
    dict.add(row[0],({"title": row[1], "description": row[2], "release_year": row[3],
                        "length": row[4], "rate": row[5], "special_features": row[6]}))

try:
    with open("film_data.json", 'x') as fd:
        json.dump([], fd, indent=4)
except FileExistsError as err:
    print("file already exists: passing")


with open('film_data.json', 'w') as json_file:
    json.dump(dict, json_file, indent=4, sort_keys=True)



#Extra

film_query = """ CREATE TABLE IF NOT EXISTS filtered_film
AS SELECT *
    FROM film_data
    where release_year > 2010 and rate BETWEEN 3 AND 5;"""

with conn:
    curs.execute(film_query)

