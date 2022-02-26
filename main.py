"""
Յու բալիկներ։ Արամ ձաձյան պարապ ա ու իրա ստրուկտուրայի տարբերակն ա մշակել
եթե տենամ դժվարանում եք, ցույց կտամ։ Բայց մեկա մինչև վերջ գրել եմ տալու, նոր կասեմ ձեզ սրա մասին ։-)
"""
from kivymd.uix.button import MDRectangleFlatIconButton
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.properties import StringProperty, ObjectProperty, ListProperty, NumericProperty, Property
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from models import get_introductions, get_description, get_name, get_sources
from functools import partial
import random, time
from kivy.clock import Clock


Window.size = (320, 600)

class ReciveFromDatabase:


	def get_sources(self, item):
		sources = []
		lessons = get_introductions(item)
		for tmp in lessons:
			sources.append(tmp)

		return sources

	def get_items(self, item):
		items = []
		lessons = get_introductions(item)
		for tmp in lessons:
			items.append(lessons[tmp])

		return items





class FirstLevelCallBacks:

	iterator = 0
	true_answers = 0

	def change_theme(self, instance):

		if self.theme_cls.theme_style == "Dark":
			self.theme_cls.theme_style = "Light"
		else:
			self.theme_cls.theme_style = "Dark"

	def lesson_callback(self, instance, lesson_sources, lesson_items):

		self.root.ids.lessons_screens_manager.current = 'lessons_more_screen'
		self.root.ids.lessons_more_widget.add_widget(LessonsBackButton())
		
		for i in range(len(lesson_items)):

			self.root.ids.lessons_more_widget.add_widget(LessonDrawer(source = lesson_sources[i], description = lesson_items[i]))


	def next_button(self, instance):
		self.iterator += 1
		self.root.ids.test_more_widget.clear_widgets()
		self.test_callback(instance, lesson_sources = self.sources, lesson_items = self.items, iterator = self.iterator)



	def test_callback(self,instance, lesson_sources, lesson_items, iterator = 0):
		
		self.root.ids.test_screens_manager.current = 'tests_more_screen'
		options = []

		self.root.ids.test_more_widget.add_widget(TestsBackButton())

		try:

			while len(options) != 4:


				rand = random.choice(lesson_items)

				if rand not in options:
					options.append(rand)

			if lesson_items[iterator] not in options:
				options[random.randint(0, len(options) - 1)] = lesson_items[iterator]

			if len(options) == 4:

				self.root.ids.test_more_widget.add_widget(TestDrawer(source = lesson_sources[iterator], options = options, true_answer = lesson_items[iterator]))

			else: 
				print(len(options))
				
		except IndexError:
			self.root.ids.test_screens_manager.current = 'tests_last_screen'

			self.root.ids.tests_last_screen.add_widget(LastTestWidget(answers = str(self.true_answers)))



	def check_answer(self, instance, true_answer, button_root):

		
		if instance.text == true_answer:
			print('True Answer!')
			self.true_answers += 1
			button_root.ids.options_layout.disabled = True
			instance.background_color = 'green'
			Clock.schedule_once(self.next_button, 1)

		else:

			print('False answer')
			instance.background_color = 'red'
			button_root.ids.options_layout.disabled = True

			Clock.schedule_once(self.next_button, 1)

		
	def get_random(self, array):

		return random.randint(0, len(array))

	def tests_back_button(self, instance):
		self.true_answers = 0
		self.root.ids.test_more_widget.clear_widgets()
		self.root.ids.test_screens_manager.current = "tests_home_screen"

	def lessons_back_button(self, instance):
		self.root.ids.lessons_more_widget.clear_widgets()
		self.root.ids.lessons_screens_manager.current = 'lessons_home_screen'

	def results_back_button(self, instance):

		self.true_answers = 0
		self.iterator = 0
		self.root.ids.tests_last_screen.clear_widgets()
		self.root.ids.test_screens_manager.current = 'tests_home_screen'



class LessonsHomeWidget(GridLayout):
	pass


class LessonsMoreWidget(GridLayout):
	pass

class LessonDrawer(GridLayout):

	source = StringProperty()
	description = StringProperty()
class LessonsBackButton(Button):
	pass


class TestsBackButton(Button):
	pass

class TestsHomeWidget(GridLayout):
	pass

class TestMoreWidget(GridLayout):
	pass

class TestDrawer(GridLayout):


	source = StringProperty()

	options = ListProperty()

	true_answer = StringProperty()

class LastTestWidget(GridLayout):
	answers = StringProperty()



class RootWidget(ScreenManager):
	pass


class MainApp(MDApp, FirstLevelCallBacks):

	window = Window.size[1]


	def on_start(self):

		# Ստեղ լցնում ենք կնոպկեքը, խոսքը համ դասերի մասին ա, համ թեստերի և այլն

		#LESSON 1 BUTTONS

		self.sources = get_sources()
		self.descriptions = get_description()
		self.names = get_name()

		lesson_1_button = MDRectangleFlatIconButton(text = f'Lesson 1', icon = '', size_hint = (1, 1), font_size = 40)
		lesson_1_button.bind(on_press = partial(self.lesson_callback, lesson_sources =  self.sources, lesson_items = self.descriptions))
		self.root.ids.lessons_home_widget.add_widget(lesson_1_button)

		test_1_button = MDRectangleFlatIconButton(text = 'Test 1', icon = '' ,size_hint = (1, 1), font_size = 40)
		test_1_button.bind(on_press = partial(self.test_callback, lesson_sources = self.sources, lesson_items = self.names))
		self.root.ids.tests_home_widget.add_widget(test_1_button)


		#LESSON 2 BUTTONS

		self.sources = ReciveFromDatabase().get_sources("Alphavite")
		self.items = ReciveFromDatabase().get_items("Alphavite")

		lesson_2_button = MDRectangleFlatIconButton(text = f'Lesson 2', icon = '', size_hint = (1, 1), font_size = 40)
		lesson_2_button.bind(on_press = partial(self.lesson_callback, lesson_sources =  self.sources, lesson_items = self.items))
		self.root.ids.lessons_home_widget.add_widget(lesson_2_button)

		test_2_button = MDRectangleFlatIconButton(text = 'Test 2', icon = '', size_hint = (1, 1), font_size = 40)
		test_2_button.bind(on_press = partial(self.test_callback, lesson_sources = self.sources, lesson_items = self.items))
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
