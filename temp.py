from posixpath import abspath
import sqlite3, os

db = sqlite3.connect('app.db')
cursor = db.cursor()

alpha = {
'ա': 'a', 'բ' : 'b', 'գ' : 'g', 'դ' : 'd',  'ե' : 'e', 'զ' : 'z', 'է' : 'e', 'ը' : 'y', 'թ' : 't', 'ժ' : 'j',
'ի' : 'i', 'լ' : 'l', 'խ' : 'x', 'ծ' : 'c', 'կ' : 'k', 'հ' : 'h', 'ձ' : 'dz', 'ղ' : 'x', 'ճ' : 'ch', 'մ' : 'm',
'յ' : 'y', 'ն' : 'n', 'շ' : 'sh', 'ո' : 'vo', 'չ' : 'ch', 'պ' : 'p', 'ջ' : 'j', 'ռ' : 'r', 'ս' : 's', 'վ' : 'v' , 'տ' : 't',
'ր' : 'r', 'ց' : 'c', 'ու' : 'u', 'փ' : 'p', 'ք' : 'q', 'և' : 'ev', 'օ' : 'o', 'ֆ' : 'f',

}


parts = ['Images/Intro', 'Images/Alphavite/', 'Images/Guyner/']

descs = ['adrbejan description', 'agah description', 'akumb description', 'albania description', 'amis description']

names = []
gifs = []


os.chdir('C:\\Users\\User\\Desktop\\KivyProject\\KivyApp\\Images\\Guyner')

for i in os.listdir():

	res = ''
	for j in i:
		if 'gif' in i:
			tm = '.gif'
		else:
			tm = '.png'
		if j in alpha:
			res += alpha[j]
	gifs.append(parts[2] + i)

	if 'gif' in i:
		names.append(i.replace('.gif', ''))
	else:
		names.append(i.replace('.png', ''))



for i in range(len(names)):
    query = f"INSERT INTO gestures(part, name, description, gif) VALUES ('{parts[2]}', '{names[i]}', 'Նկարագրություն', '{gifs[i]}')"
    cursor.execute(query)
db.commit()

# info = cursor.execute("SELECT * FROM gestures")
# print(info.fetchall())
