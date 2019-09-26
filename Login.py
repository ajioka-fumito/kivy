from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
Config.set('graphics', 'width', '960')
Config.set('graphics', 'height', '640')
from kivy.properties import StringProperty 

from kivy.core.window import Window
from kivy.factory import Factory
from kivy.uix.textinput import TextInput

class Login(FloatLayout):
