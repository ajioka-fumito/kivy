from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
Config.set('graphics', 'width', '960')
Config.set('graphics', 'height', '640')
from kivy.properties import StringProperty 

from kivy.core.window import Window
from kivy.factory import Factory
from kivy.uix.textinput import TextInput

from kivy.lang import Builder
Builder.load_file('./Login.kv')



class MainWidget(FloatLayout):
    source = StringProperty("./images/sample.jpg")
    def __init__(self, **kwargs):
        #self.Login = Factory.Login()
        super(MainWidget, self).__init__(**kwargs)
        

    def buttonClicked_Login(self):
        self.clear_widgets()
        self.add_widget(self.Login)



class MainApp(App):
    def __init__(self, **kwargs):
        super(MainApp,self).__init__(**kwargs)
        self.title = "ajioka fumito"

    def build(self):
        return MainWidget()

if __name__=="__main__":
    MainApp().run()