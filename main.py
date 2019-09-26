from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
Config.set('graphics', 'width', '960')
Config.set('graphics', 'height', '640')
from kivy.properties import StringProperty 

from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class MainWidget(FloatLayout):
    source = StringProperty("./images/sample.jpg")    # プロパティの追加

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)

    def buttonClicked(self):
        self.source = "./images/sample1.jpg"



class MainApp(App):
    def __init__(self, **kwargs):
        super(MainApp,self).__init__(**kwargs)
        self.title = "ajioka fumito"

    def build(self):
        return MainWidget()

if __name__=="__main__":
    MainApp().run()