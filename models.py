import os
import sqlite3

def searchByName(item):
    
    query = f"SELECT * FROM gestures where name like '%{item}%'"

    data = cursor.execute(query).fetchall()

    return data

    

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


def delete_from_favorites(item):

    query = "DELETE FROM favorites WHERE name = '{}'".format(item)
    cursor.execute(query)
    db.commit()





    


