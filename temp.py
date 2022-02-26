from posixpath import abspath
import sqlite3, os

db = sqlite3.connect('app.db')
cursor = db.cursor()




parts = ['Images/Intro', 'Images/Alphavite/']

descs = ['adrbejan description', 'agah description', 'akumb description', 'albania description', 'amis description']

names = []
gifs = []
for i in os.listdir(parts[1]):
    names.append(i.replace('.gif', ''))
    gifs.append(parts[1] + i)


for i in range(len(descs)):
    query = f"INSERT INTO gestures(part, name, description, gif) VALUES ('{parts[1]}', '{names[i]}', '{descs[i]}', '{gifs[i]}')"
    cursor.execute(query)
db.commit()

info = cursor.execute("SELECT * FROM gestures")
print(info.fetchall())
