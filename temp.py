from posixpath import abspath
import sqlite3, os

db = sqlite3.connect('app.db')
cursor = db.cursor()




parts = ['Images/Intro', 'Images/Alphavite/', 'Images/Ashxarh/']

descs = ['adrbejan description', 'agah description', 'akumb description', 'albania description', 'amis description']

names = []
gifs = []
for i in os.listdir(parts[2]):
    names.append(i.replace('.gif', ''))
    gifs.append(parts[2] + i)

print(names, gifs)

for i in range(len(names)):
    query = f"INSERT INTO gestures(part, name, description, gif) VALUES ('{parts[2]}', '{names[i]}', 'Նկարագրություն', '{gifs[i]}')"
    cursor.execute(query)
db.commit()

info = cursor.execute("SELECT * FROM gestures")
print(info.fetchall())
