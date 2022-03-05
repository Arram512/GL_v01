"""
Յու բալիկներ։ Արամ ձաձյան պարապ ա ու իրա ստրուկտուրայի տարբերակն ա մշակել
եթե տենամ դժվարանում եք, ցույց կտամ։ Բայց մեկա մինչև վերջ գրել եմ տալու, նոր կասեմ ձեզ սրա մասին ։-)
"""

from typing import List
from kivymd.uix.dialog.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatIconButton
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.properties import StringProperty, ObjectProperty, ListProperty, NumericProperty, Property
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from models import get_introductions, get_description, get_name, get_sources, add_to_favorites, get_from_favorites
from functools import partial
import random, time
from kivy.clock import Clock
from kivymd.uix.label import MDLabel


Window.size = (320, 600)



class FirstLevelCallBacks:

	true_answers = 0

	
	def filling_favorites(self):

		self.favorite_callback(names = get_from_favorites()[0], descriptions= get_from_favorites()[2], sources= get_from_favorites()[1])



	def add_to_favorite(self, instance):
		
		add_to_favorites(name = instance.name, source = instance.source, description= instance.description)
		self.filling_favorites()

	def favorite_callback(self, sources, names, descriptions, iterator = 0):
		try:
			self.root.ids.favorites_bottom_navigation_item.clear_widgets()
			self.root.ids.favorites_bottom_navigation_item.add_widget(FavoritesDrawer(iterator = iterator, names = names, sources = sources, descriptions = descriptions, name = names[iterator], source = sources[iterator], description = descriptions[iterator]))
		except IndexError:
			print('index out of range')

	def change_theme(self, instance):

		if self.theme_cls.theme_style == "Dark":
			self.theme_cls.theme_style = "Light"
		else:
			self.theme_cls.theme_style = "Dark"

	def lesson_callback(self, instance, lesson_sources, lesson_items, lesson_names, iterator = 0):

		self.root.ids.lessons_screens_manager.current = 'lessons_more_screen'
		self.root.ids.lessons_more_widget.clear_widgets()

		try:
			if iterator >= 0:
				self.root.ids.lessons_more_widget.add_widget(LessonDrawer(iterator = iterator, lesson_names = lesson_names, lesson_descriptions = lesson_items, lesson_sources = lesson_sources, name = lesson_names[iterator],source = lesson_sources[iterator], description = lesson_items[iterator]))
				print(lesson_sources[iterator])
			else:
				pass
		except:
			if iterator >= len(lesson_sources):
				self.root.ids.lessons_more_widget.clear_widgets()
				self.root.ids.lessons_more_widget.add_widget(Button(text = 'End lesson'))




	def test_callback(self,instance, lesson_sources, lesson_items,  iterator = 0, *args, **kwargs):

		
		self.root.ids.test_screens_manager.current = 'tests_more_screen'
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
				self.root.ids.test_more_widget.add_widget(TestDrawer( iterator = iterator, test_sources = lesson_sources, test_names = lesson_items, source = lesson_sources[iterator], options = options, true_answer = lesson_items[iterator], count = str(self.true_answers)))

			else: 
				print(len(options))
				
		except IndexError:
			self.root.ids.test_screens_manager.current = 'tests_last_screen'

			self.root.ids.tests_last_screen.add_widget(LastTestWidget(answers = str(self.true_answers)))



	def check_answer(self, instance, true_answer, button_root, names, sources):


		
		if instance.text == true_answer:
			print(button_root.ids.test_image.source)
			self.true_answers += 1
			instance.md_bg_color_disabled = 'green'
			button_root.ids.options_layout.disabled = True
			Clock.schedule_once(partial(self.test_callback, instance, sources, names, button_root.iterator + 1), 1) #breakpoint 

		else:

			print('False answer')
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

			Clock.schedule_once(partial(self.test_callback, instance, sources, names, button_root.iterator + 1), 1) #breakpoint 

		
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




class LessonsHomeWidget(GridLayout):
	pass


class LessonsMoreWidget(GridLayout):
	pass

class LessonDrawer(MDBoxLayout):

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


	iterator = NumericProperty()

	test_sources = ListProperty()

	test_names = ListProperty()

	source = StringProperty()

	options = ListProperty()

	true_answer = StringProperty()

	count = StringProperty()

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


class MainApp(MDApp, FirstLevelCallBacks):


	window = Window.size[1]

	font_name = './FreeSans.ttf'


	def on_start(self):

		# Ստեղ լցնում ենք կնոպկեքը, խոսքը համ դասերի մասին ա, համ թեստերի և այլն


		self.filling_favorites()


		#LESSON 1 BUTTONS

		self.sources = get_sources('Alphavite')
		self.descriptions = get_description('Alphavite')
		self.names = get_name('Alphavite')


		lesson_1_button = MDRectangleFlatIconButton(text = f'Lesson 1', icon = '', size_hint = (1, 1))
		lesson_1_button.bind(on_press = partial(self.lesson_callback, lesson_sources =  self.sources, lesson_items = self.descriptions, lesson_names = self.names))
		self.root.ids.lessons_home_widget.add_widget(lesson_1_button)

		test_1_button = MDRectangleFlatIconButton(text = 'Test 1', icon = '' ,size_hint = (1, 1))
		test_1_button.bind(on_press = partial(self.test_callback, lesson_sources = self.sources, lesson_items = self.names))
		self.root.ids.tests_home_widget.add_widget(test_1_button)

		self.root.ids.favorites_toolbar.ids.label_title.font_name = self.root.ids.tests_more_screen_toolbar.ids.label_title.font_name = self.font_name
		#breakpoint


		#LESSON 2 BUTTONS

		self.sources = get_sources("Alphavite")
		self.items = get_description("Alphavite")
		self.names = get_name('Alphavite')

		lesson_2_button = MDRectangleFlatIconButton(text = f'Lesson 2', icon = '', size_hint = (1, 1))
		lesson_2_button.bind(on_press = partial(self.lesson_callback, lesson_sources =  self.sources, lesson_items = self.items))
		self.root.ids.lessons_home_widget.add_widget(lesson_2_button)

		test_2_button = MDRectangleFlatIconButton(text = 'Test 2', icon = '', size_hint = (1, 1))
		test_2_button.bind(on_press = partial(self.test_callback, lesson_sources = self.sources, lesson_items = self.names))
		self.root.ids.tests_home_widget.add_widget(test_2_button)

		# lesson_3_button = MDRectangleFlatIconButton(text = f'Lesson 3', size_hint = (1, 1), font_size = 40)
		# lesson_3_button.bind(on_press = partial(self.lesson_callback, lesson_sources =  self.sources[4:], lesson_items = self.items[4:]))
		# self.root.ids.lessons_home_widget.add_widget(lesson_3_button)

		# lesson_4_button = MDRectangleFlatIconButton(text = f'Lesson 4', size_hint = (1, 1), font_size = 40)
		# lesson_4_button.bind(on_press = partial(self.lesson_callback, lesson_sources =  self.sources[4:], lesson_items = self.items[4:]))
		# self.root.ids.lessons_home_widget.add_widget(lesson_4_button)

		# lesson_5_button = MDRectangleFlatIconButton(text = f'Lesson 5',size_hint = (1, 1), font_size = 40)
		# lesson_5_button.bind(on_press = partial(self.lesson_callback, lesson_sources =  self.sources[4:], lesson_items = self.items[4:]))
		# self.root.ids.lessons_home_widget.add_widget(lesson_5_button)

		# lesson_6_button = MDRectangleFlatIconButton(text = f'Lesson 6', size_hint = (1, 1), font_size = 40)
		# lesson_6_button.bind(on_press = partial(self.lesson_callback, lesson_sources =  self.sources[4:], lesson_items = self.items[4:]))
		# self.root.ids.lessons_home_widget.add_widget(lesson_6_button)

		# lesson_7_button = MDRectangleFlatIconButton(text = f'Lesson 7', size_hint = (1, 1), font_size = 40)
		# lesson_7_button.bind(on_press = partial(self.lesson_callback, lesson_sources =  self.sources[4:], lesson_items = self.items[4:]))
		# self.root.ids.lessons_home_widget.add_widget(lesson_7_button)





		###################################################################################################################

		#TEST BUTTONS








		# test_3_button = MDRectangleFlatIconButton(text = 'Test 3', size_hint = (1, 1), font_size = 40)
		# test_3_button.bind(on_press = partial(self.test_callback, lesson_sources = self.sources[4:], lesson_items = self.items[4:]))
		# self.root.ids.tests_home_widget.add_widget(test_3_button)

		# test_4_button = MDRectangleFlatIconButton(text = 'Test 4', size_hint = (1, 1), font_size = 40)
		# test_4_button.bind(on_press = partial(self.test_callback, lesson_sources = self.sources[4:], lesson_items = self.items[4:]))
		# self.root.ids.tests_home_widget.add_widget(test_4_button)

		# test_5_button = MDRectangleFlatIconButton(text = 'Test 5', size_hint = (1, 1), font_size = 40)
		# test_5_button.bind(on_press = partial(self.test_callback, lesson_sources = self.sources[4:], lesson_items = self.items[4:]))
		# self.root.ids.tests_home_widget.add_widget(test_5_button)

		# test_6_button = MDRectangleFlatIconButton(text = 'Test 6', size_hint = (1, 1), font_size = 40)
		# test_6_button.bind(on_press = partial(self.test_callback, lesson_sources = self.sources[4:], lesson_items = self.items[4:]))
		# self.root.ids.tests_home_widget.add_widget(test_6_button)

		# test_7_button = MDRectangleFlatIconButton(text = 'Test 7', size_hint = (1, 1), font_size = 40)
		# test_7_button.bind(on_press = partial(self.test_callback, lesson_sources = self.sources[4:], lesson_items = self.items[4:]))
		# self.root.ids.tests_home_widget.add_widget(test_7_button)





		##################################################################################################################



	def build(self):
		pass



if __name__ == '__main__':
	MainApp().run()
