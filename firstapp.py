import kivy
from kivy.app import App

from kivy.uix.label import Label  #For text

kivy.require("1.10.1")

class MyApp(App):
	def build(self):
		return Label(text="Hello There!")

if __name__ == '__main__':
	MyApp().run()