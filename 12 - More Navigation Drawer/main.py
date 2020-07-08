from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList

from navigation_drawer import navigation_helper

Window.size = (300, 500)


class DemoApp(MDApp):
    class ContentNavigationDrawer(BoxLayout):
        pass

    class DrawerList(ThemableBehavior, MDList):
        pass

    def build(self):
        screen = Builder.load_string(navigation_helper)
        return screen

    def on_start(self):
        pass


DemoApp().run()
