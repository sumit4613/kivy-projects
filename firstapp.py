import kivy
from kivy.app import App

from kivy.uix.label import Label  #For rendering text
from kivy.uix.gridlayout import GridLayout  # widgets
from kivy.uix.textinput import TextInput  #input text from user 

kivy.require("1.10.1")

class ConnectPage(GridLayout):
	"""docstring for ConnectPage"""
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.cols = 2

		self.add_widget(Label(text="IP:"))

		self.ip = TextInput(multiline=False)
		self.add_widget(self.ip)

		self.add_widget(Label(text="Port:"))

		self.port = TextInput(multiline=False)
		self.add_widget(self.port)
		
		self.add_widget(Label(text="Username:"))

		self.username = TextInput(multiline=False)
		self.add_widget(self.username)
		
		


class DemoApp(App):
	def build(self):
		return ConnectPage()

if __name__ == '__main__':
	DemoApp().run()