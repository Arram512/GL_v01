import os
import sqlite3

def get_introductions(item):
    lessons_a = {}
    path = os.path.dirname(os.path.abspath(__file__))
    dir = f"\\Images\\{item}\\"
    gifs = os.listdir(path + dir)
    for i in range(len(gifs)):
        gif = gifs[i].split('.')[0]
        lessons_a[path + dir + gifs[i]] = f"{gif}"

    return lessons_a

db = sqlite3.connect('app.db')
cursor = db.cursor()

def get_description():
    query = "SELECT description FROM gestures where part = 'Images/Alphavite/'"

    data = cursor.execute(query).fetchall()

    descriptions = [case[0] for case in data]

    return descriptions

def get_name():

    query = "SELECT name FROM gestures where part = 'Images/Alphavite/'"

    data = cursor.execute(query).fetchall()

    names = [case[0] for case in data]

    return names

def get_sources():

    query = "SELECT gif FROM gestures where part = 'Images/Alphavite/'"

    data = cursor.execute(query).fetchall()

    path = os.path.dirname(os.path.abspath(__file__))


    sources = [path + "\\" +case[0].replace('/', '\\') for case in data]


    return sources


    


