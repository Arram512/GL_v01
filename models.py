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

def get_description(folder):
    query = "SELECT description FROM gestures where part = 'Images/{}/'".format(folder)

    data = cursor.execute(query).fetchall()

    descriptions = [case[0] for case in data]

    return descriptions

def get_name(folder):

    query = "SELECT name FROM gestures where part = 'Images/{}/'".format(folder)

    data = cursor.execute(query).fetchall()

    names = [case[0] for case in data]

    return names

def get_sources(folder):

    query = "SELECT gif FROM gestures where part = 'Images/{}/'".format(folder)

    data = cursor.execute(query).fetchall()

    path = os.path.dirname(os.path.abspath(__file__))


    sources = [path + "\\" +case[0].replace('/', '\\') for case in data]


    return sources


def add_to_favorites(name, source, description):

    query = " INSERT INTO favorites (name, source, description) VALUES ('{}', '{}', '{}') ".format(name, source, description)
    cursor.execute(query)
    db.commit()

    print(name, source, description)

def get_from_favorites():

    query = "SELECT * FROM favorites"
    data = cursor.execute(query).fetchall()
    
    favorite_names = []
    favorite_sources = []
    favorite_descriptions = []

    for i in range(len(data)):
        
        favorite_names.append(data[i][1])
        favorite_sources.append(data[i][2])
        favorite_descriptions.append(data[i][3])

    return favorite_names, favorite_sources, favorite_descriptions








    


