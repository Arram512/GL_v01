from kivymd.uix.dialog.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatIconButton
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.lang.builder import Builder
from kivy.properties import StringProperty, ObjectProperty, ListProperty, NumericProperty, Property
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from models import get_description, get_name, get_sources, add_to_favorites, get_from_favorites, delete_from_favorites, searchByName
from functools import partial
import random, time
from kivy.clock import Clock
from kivymd.uix.label import MDLabel
import os, string 
from hangman import HangmanApp, MyRoot
#from dulwich import porcelain





class FirstLevelCallBacks:

	true_answers = 0


	def search_gesture_in_database(self, gesture_name, language):

		self.root.ids.search_name.text = ''
		result = searchByName(gesture_name, language)
		names = []
		descriptions = []
		sources = []
		if len(result) > 0:
			for item in result:
				names.append(item[0])
				descriptions.append(item[1])
				sources.append(item[2])

		self.lesson_callback(self, sources, descriptions, names)
		self.root.ids.bottom_navigation.ids.tab_manager.current = 'lessons_item'

	
	def filling_favorites(self):

		self.root.ids.favorites_home_widget.clear_widgets()


		self.favorite_gestures_list(names = get_from_favorites()[0], descriptions= get_from_favorites()[2], sources= get_from_favorites()[1])



	def add_to_favorite(self, instance):

		names = get_from_favorites()[0]
		if instance.name not in names:
			add_to_favorites(name = instance.name, source = instance.source, description= instance.description)
			self.filling_favorites()
		else:
			pass

	def delete_from_favorite(self, instance):
		
		delete_from_favorites(instance)
		self.filling_favorites()

	def favorite_gestures_list(self, sources, names, descriptions):

		self.root.ids.favorites_screens_manager.current = 'favorites_home_screen'


		for i in range(len(names)):
			temp = MDRectangleFlatButton(text = names[i], font_name = MainApp().font_name, size_hint = (1,1))
			temp.bind(on_press = partial(self.favorite_callback, sources , names,  descriptions, iterator = i))
			self.root.ids.favorites_home_widget.add_widget(temp)


	def favorite_callback(self, sources, names, descriptions, root = ObjectProperty(), iterator = 0):

		self.root.ids.favorites_screens_manager.current = 'favorites_more_screen'

		try:
			if iterator < 0:
				root.ids.favorite_previouse_button.disabled = True
			elif iterator >= 0 and iterator < len(names):
				self.root.ids.favorites_more_widget.clear_widgets()
				self.root.ids.favorites_more_widget.add_widget(FavoritesDrawer(iterator = iterator, names = names, sources = sources, descriptions = descriptions, name = names[iterator], source = sources[iterator], description = descriptions[iterator]))
			elif iterator>= len(names):
				root.ids.favorite_next_button.disabled = True


		except:
			pass

	def change_theme(self, instance):

		if self.theme_cls.theme_style == "Dark":
			self.theme_cls.theme_style = "Light"
		else:
			self.theme_cls.theme_style = "Dark"

	def lesson_callback(self, instance, lesson_sources, lesson_items, lesson_names, root = ObjectProperty(), iterator = 0, title = ''):

		self.root.ids.lessons_screens_manager.current = 'lessons_more_screen'
		self.root.ids.lessons_more_toolbar.title = title

		try:

			if iterator < 0:
				root.ids.lesson_previouse_button.disabled = True

			elif iterator >= 0 and iterator < len(lesson_names):

				self.root.ids.lessons_more_widget.clear_widgets()
				self.root.ids.lessons_more_widget.add_widget(LessonDrawer(title = title, iterator = iterator, lesson_names = lesson_names, lesson_descriptions = lesson_items, lesson_sources = lesson_sources, name = lesson_names[iterator],source = lesson_sources[iterator], description = lesson_items[iterator]))

			elif iterator>= len(lesson_names):
				root.ids.lesson_next_button.disabled = True

		except Exception as ex:

			pass
			



	def test_callback(self,instance, lesson_sources, lesson_items,  iterator = 0, title = '', *args, **kwargs):

		
		self.root.ids.test_screens_manager.current = 'tests_more_screen'
		self.root.ids.tests_more_screen_toolbar.title = title
		self.root.ids.test_more_widget.clear_widgets()

		options = []


		try:

			while len(options) != 4:


				rand = random.choice(lesson_items)

				if rand not in options:
					options.append(rand)

			if lesson_items[iterator] not in options:
				options[random.randint(0, len(options) - 1)] = lesson_items[iterator]

			if len(options) == 4:
				self.root.ids.test_more_widget.add_widget(TestDrawer(title = title , iterator = iterator, test_sources = lesson_sources, test_names = lesson_items, source = lesson_sources[iterator], options = options, true_answer = lesson_items[iterator], count = str(self.true_answers)))

			else: 
				pass
				
		except IndexError:
			self.root.ids.test_screens_manager.current = 'tests_last_screen'

			self.root.ids.tests_last_screen.add_widget(LastTestWidget(answers = str(self.true_answers)))



	def check_answer(self, instance, true_answer, button_root, names, sources):

		
		if instance.text == true_answer:
			self.true_answers += 1
			instance.md_bg_color_disabled = 'green'
			button_root.ids.options_layout.disabled = True
			Clock.schedule_once(partial(self.test_callback, instance, sources, names, button_root.iterator + 1, button_root.title), 1) #breakpoint 

		else:

			instance.md_bg_color_disabled = 'red'

			if button_root.ids.button_1.text == true_answer:
				button_root.ids.button_1.md_bg_color_disabled = 'green'
			elif button_root.ids.button_2.text == true_answer:
				button_root.ids.button_2.md_bg_color_disabled = 'green'
			elif button_root.ids.button_3.text == true_answer:
				button_root.ids.button_3.md_bg_color_disabled = 'green'
			elif button_root.ids.button_4.text == true_answer:
				button_root.ids.button_4.md_bg_color_disabled = 'green'

			button_root.ids.options_layout.disabled = True
			Clock.schedule_once(partial(self.test_callback, instance, sources, names, button_root.iterator + 1, button_root.title), 1) #breakpoint 

		
	def get_random(self, array):

		return random.randint(0, len(array))

	def tests_back_button(self, instance):

		self.true_answers = 0
		self.root.ids.tests_last_screen.clear_widgets()

		self.root.ids.test_more_widget.clear_widgets()
		self.root.ids.test_screens_manager.current = "tests_home_screen"

	def lessons_back_button(self, instance):

		self.root.ids.lessons_more_widget.clear_widgets()

		self.root.ids.lessons_screens_manager.current = 'lessons_home_screen'

	def favorites_back_button(self):

		self.root.ids.favorites_screens_manager.current = 'favorites_home_screen'




class LessonsHomeWidget(GridLayout):
	pass


class LessonsMoreWidget(GridLayout):
	pass

class LessonDrawer(MDBoxLayout):

	title = StringProperty()

	iterator = NumericProperty()


	lesson_names = ListProperty()
	lesson_sources = ListProperty()
	lesson_descriptions = ListProperty()
	source = StringProperty()
	description = StringProperty()
	name = StringProperty()


class TestsHomeWidget(GridLayout):
	pass

class TestMoreWidget(GridLayout):
	pass



class TestDrawer(MDBoxLayout):



	title = StringProperty()

	iterator = NumericProperty()

	test_sources = ListProperty()

	test_names = ListProperty()

	source = StringProperty()

	options = ListProperty()

	true_answer = StringProperty()

	count = StringProperty()

	next_button = StringProperty()

class LastTestWidget(MDBoxLayout):
	answers = StringProperty()


class FavoritesDrawer(MDBoxLayout):

	iterator = NumericProperty()

	names = ListProperty()
	sources = ListProperty()
	descriptions = ListProperty()

	name = StringProperty()
	source = StringProperty()
	description = StringProperty()


class RootWidget(ScreenManager):
	pass



class WelcomeScreen(MDApp):

	def loader(self):
		#porcelain.clone("https://github.com/Arram512/Animations", os.getcwd() + "/Images/")
		self.root.ids.button.text = '?????????????????????? ???????? ??????????'
	
	def build(self):
		return Builder.load_file('./kv/welcome.kv')


class MainApp(MDApp, FirstLevelCallBacks):


	width = Window.size[0]
	height = Window.size[1]

	LANGUAGE = ""


	font_name = './FreeSans.ttf'


	lesson_home_title = {"" : "??????????", "ru_": "??????????", "en_":"Lessons"}

	test_home_title = {"" : "????????????", "ru_": "??????????", "en_":"Tests"}

	favorites_home_title = {"" : "????????????????????", "ru_": "??????????????????", "en_":"Favorites"}

	settings_home_title = {"": "????????????????????????????", "ru_": "??????????????????", "en_":"Settings"}
	
	next_button = {"": "??????????????", "ru_":"??????????????????", "en_":"Next"}

	previouse_button = {"": "??????????????", "ru_": "????????????????????", "en_": "Previouse"}

	add_favorite = {"": "?????????????? ??????????????", "ru_":"???????????????? ?? ??????????????????", "en_":"Add to Favorites"}

	drop_favorite = {"": "????????????????", "ru_":"??????????????", "en_":"Delete"}



	def restart(self):
		self.root.clear_widgets()
		self.root.add_widget(MyRoot())




	def change_language(self, language):

		self.root.ids.lessons_home_widget.clear_widgets()
		self.root.ids.tests_home_widget.clear_widgets()

		self.LANGUAGE = language

		self.on_start()






	def on_start(self):
		



		self.filling_favorites()


		self.root.ids.lessons_home_toolbar.title = self.lesson_home_title[self.LANGUAGE]
		self.root.ids.tests_home_toolbar.title = self.test_home_title[self.LANGUAGE]
		self.root.ids.favorites_home_toolbar.title = self.favorites_home_title[self.LANGUAGE]
		self.root.ids.favorites_more_toolbar.title = self.favorites_home_title[self.LANGUAGE]
		self.root.ids.settings_home_toolbar.title = self.settings_home_title[self.LANGUAGE]



		
		self.root.ids.favorites_home_toolbar.ids.label_title.font_name = self.font_name
		self.root.ids.favorites_more_toolbar.ids.label_title.font_name = self.font_name
		self.root.ids.tests_more_screen_toolbar.ids.label_title.font_name = self.font_name
		self.root.ids.lessons_home_toolbar.ids.label_title.font_name = self.font_name
		self.root.ids.lessons_more_toolbar.ids.label_title.font_name = self.font_name
		self.root.ids.tests_home_toolbar.ids.label_title.font_name = self.font_name
		self.root.ids.settings_home_toolbar.ids.label_title.font_name = self.font_name


		parts = [
			'',
			'Alphavite',
			'Tver',
			'Guyner',
			'Canotuttyn',
			'Jamanak',
			'Bjshkutyun',
			'Tun',
			'Hagust',
			'Kendaniner',
			'Masnagitutyun',
			'Orenq',
			'Sport',
			'Ashxarh',
			'Kron',
			'Mard',
			'Tohmacar',


			]


		part_names = {"":[
			'????????????????????????', 
			'????????????????',
			'????????',
			"??????????????",
			'????????????????????????',
			'??????????????',
			"??????????????????????",
			'????????, ?????? ??????????????????',
			"??????????????",
			"????????????????????",
			"????????????????, ??????????????????????????????",
			"??????????, ????????????????",
			"??????????, ??????????????",
			'????????????',
			"????????",
			'????????',
			'??????????????, ????????????????????????????',
			'??????????????????',
			'???????????????? ????????????????????????????????????',
			"??????????????????, ????????????????????????",
			],

			"ru_": [
				'????????????????',
				'??????????????',
				'??????????',
				'??????????',
				'????????????????????',
				'??????????',
				'????????????????',
				'??????, ???????????????? ????????',
				'????????????, ???????????????? ????????????',
				'????????????????',
				'????????????. ??????????????????',
				'??????????, ??????????',
				'??????????, ??????????',
				'??????. ??????????????????????. ????????????',
				'??????????????, ????????',
				'??????????????',
				'??????????, ??????',
				'??????????????',
				'???????????????????????????????? ??????????????????',
				'????????????, ??????????????',
			],

			"en_": [
				'Introduction',
				'Alphabet',
				'Numbers',
				'Colors',
				'Acquaintance',
				'Time',
				'The medicine',
				'House, household things',
				'Clothes, elements of clothing',
				'Animals',
				'Work. Profession',
				'Law, right',
				'Sport, recreation',
				'Peace. States. Cities',
				'Religion, faith',
				'Human',
				'Family',
				'Nature',
				'Expanded Expressions',
				'Emotions, feelings',
			]

			}


		for item in range(len(part_names[self.LANGUAGE])):

			try:

				sources = get_sources(parts[item])
				descriptions = get_description(parts[item], self.LANGUAGE)
				names = get_name(parts[item], self.LANGUAGE)

				lesson_1_button = MDRectangleFlatIconButton(text = part_names[self.LANGUAGE][item], icon = '', size_hint = (1, 1), font_name = self.font_name, md_bg_color = (255, 255, 206, 1), text_color = (0, 0, 0, 1))
				lesson_1_button.bind(on_press = partial(self.lesson_callback, lesson_sources =  sources, lesson_items = descriptions, lesson_names = names, title = lesson_1_button.text))
				self.root.ids.lessons_home_widget.add_widget(lesson_1_button)

				test_1_button = MDRectangleFlatIconButton(text = part_names[self.LANGUAGE][item], icon = '' ,size_hint = (1, 1), font_name = self.font_name, md_bg_color = (255, 255, 206, 1), text_color = (0, 0, 0, 1))
				test_1_button.bind(on_press = partial(self.test_callback, lesson_sources = sources, lesson_items = names, title = test_1_button.text))
				self.root.ids.tests_home_widget.add_widget(test_1_button)
			except:
				lesson_1_button = MDRectangleFlatIconButton(text = part_names[self.LANGUAGE][item], icon = '', size_hint = (1, 1), font_name = self.font_name)
				self.root.ids.lessons_home_widget.add_widget(lesson_1_button)

				test_1_button = MDRectangleFlatIconButton(text = part_names[self.LANGUAGE][item], icon = '' ,size_hint = (1, 1), font_name = self.font_name)
				self.root.ids.tests_home_widget.add_widget(test_1_button)





	def build(self):
		pass



if 'Images' not in os.listdir():
	WelcomeScreen().run()
else:
	MainApp().run()
