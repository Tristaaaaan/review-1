from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Pink"
        screen = Builder.load_file('screenmanager.kv')
        return screen


class IntroScreen(Screen):
    pass


class GameScreen(Screen):
    pass


class EndScreen(Screen):
    pass


DemoApp().run()
