import os
import sqlite3



db = sqlite3.connect('app.db')
cursor = db.cursor()

def get_words():
    query = f"SELECT name, gif FROM gestures"

    data = cursor.execute(query).fetchall()


    WORDS = [[], []]

    for word in data:
        if "և" in word[0]:
            word[0].replace('և', 'եվ')
        WORDS[0].append(word[0].strip())
        WORDS[1].append(word[1])

    return WORDS


    
