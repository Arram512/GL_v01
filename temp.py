from posixpath import abspath
import sqlite3, os, random

db = sqlite3.connect('app.db')
cursor = db.cursor()

alpha = {
'ա': 'a', 'բ' : 'b', 'գ' : 'g', 'դ' : 'd',  'ե' : 'e', 'զ' : 'z', 'է' : 'e', 'ը' : 'y', 'թ' : 't', 'ժ' : 'j',
'ի' : 'i', 'լ' : 'l', 'խ' : 'x', 'ծ' : 'c', 'կ' : 'k', 'հ' : 'h', 'ձ' : 'dz', 'ղ' : 'x', 'ճ' : 'ch', 'մ' : 'm',
'յ' : 'y', 'ն' : 'n', 'շ' : 'sh', 'ո' : 'vo', 'չ' : 'ch', 'պ' : 'p', 'ջ' : 'j', 'ռ' : 'r', 'ս' : 's', 'վ' : 'v' , 'տ' : 't',
'ր' : 'r', 'ց' : 'c', 'ու' : 'u', 'փ' : 'p', 'ք' : 'q', 'և' : 'ev', 'օ' : 'o', 'ֆ' : 'f',

}


parts = ['Images/Intro', 'Images/Alphavite/', 'Images/Tver/']

descs = ['adrbejan description', 'agah description', 'akumb description', 'albania description', 'amis description']

names = []
gifs = []


# os.chdir('C:\\Users\\User\\Desktop\\KivyProject\\KivyApp\\Images\\Tver')


# a = 'qwertyuiopasdfghjklzxcvbnm'
# nums = '1234567890'

# r = ['gif', 'png']

# for i in os.listdir():

# 	res = ''

# 	if 'gif' in i:
# 		names.append(i.replace('.gif', ''))
# 	else:
# 		names.append(i.replace('.png', ''))

# 	if 'gif' in i:
# 		tm = '.gif'
# 	else:
# 		tm = '.png'

# 	for j in i:

# 		if j in nums:
# 			res = i
# 			continue


# 		if j.lower() in alpha:
# 			res += alpha[j.lower()]

# 	if res[-3:] not in r:
# 		gifs.append(parts[2] + res + tm)
# 	else:
# 		gifs.append(parts[2] + res)


# 	# res = parts[2] + res + tm

# 	# if res in gifs:
# 	# 	res = res[:len(res) - 4] + '1' + random.choice(a) + '.gif'
# 	# os.rename(i, res.split('/')[2])


# print(len(gifs), len(names))
# print(gifs, names)



# for i in range(len(gifs)):
#     query = f"INSERT INTO gestures(part, name, description, gif) VALUES ('{parts[2]}', '{names[i]}', 'Նկարագրություն', '{gifs[i]}')"
#     cursor.execute(query)
# db.commit()

# for i in range(len(gifs)):
#     query = f"UPDATE gestures SET gif = '{gifs[i]}' where name like '%{names[i].strip()}%'"
#     cursor.execute(query)
# db.commit()

# info = cursor.execute("SELECT * FROM gestures where part = 'Images/Ashxarh/'")
# data = info.fetchall()
# print(data)

with open('text.txt', 'r', encoding  = 'utf-8') as file:

	for line in file.readlines():
		#print(line.split('-'))
		name, description = line.split('-')
		print(name, description)
		description = description[1].title() + description[2:]
		query = "UPDATE gestures SET description = '{}' where name like '%{}%'".format(description, name.strip())
		#query = 'SELECT * from gestures where name = "{}"'.format(name.strip())
		z = cursor.execute(query)
		#print(z.fetchall())

db.commit()

# for item in data:
# 	print(item)
