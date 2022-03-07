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


parts = ['Images/Intro', 'Images/Alphavite/', 'Images/Jamanak/']

descs = ['adrbejan description', 'agah description', 'akumb description', 'albania description', 'amis description']

names = []
gifs = []


os.chdir('C:\\Users\\User\\Desktop\\KivyProject\\KivyApp\\Images\\Jamanak')


for i in os.listdir():

	res = ''
	for j in i:
		if 'gif' in i:
			tm = '.gif'
		else:
			tm = '.png'
		if j in alpha:
			res += alpha[j]
	os.rename(i, res + tm)

# 	if 'gif' in i:
# 		names.append(i.replace('.gif', ''))
# 	else:
# 		names.append(i.replace('.png', ''))

# print(gifs, names)



# for i in range(len(gifs)):
#     query = f"INSERT INTO gestures(part, name, description, gif) VALUES ('{parts[2]}', '{names[i]}', 'Նկարագրություն', 'gif')"
#     cursor.execute(query)
# db.commit()
# for i in range(len(gifs)):
#     query = f"UPDATE gestures SET gif = '{gifs[i]}' where name like '%{names[i].strip()}%'"
#     cursor.execute(query)
# db.commit()

# info = cursor.execute("SELECT * FROM gestures where part = 'Images/Ashxarh/'")
# data = info.fetchall()
# print(data)

# with open('text.txt', 'r', encoding  = 'utf-8') as file:

# 	for line in file.readlines():
# 		name, description = line.split('-')
# 		description = description[1].title() + description[2:]
# 		print(name, description)
# 		query = "UPDATE gestures SET description = '{}' where name like '%{}%'".format(description, name.strip())
# 		cursor.execute(query)

# db.commit()

# for item in data:
# 	print(item)
