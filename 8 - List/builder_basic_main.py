from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder

list_helper = """
ScrollView:
    MDList:
        OneLineListItem:
            text: 'Item1'
        OneLineListItem:
            text: 'Item2'
"""


class DemoApp(MDApp):

    def build(self):
        screen = Screen()
        list_item = Builder.load_string(list_helper)
        screen.add_widget(list_item)
        return screen


DemoApp().run()
