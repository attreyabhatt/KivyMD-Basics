from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivy.core.window import Window

Window.size = (360, 600)


class DemoApp(MDApp):
    def build(self):
        screen = Screen()

        username = MDTextField(text="Enter Weight",
                               helper_text="This will disappear when you click off",
                               helper_text_mode="on_focus",
                               pos_hint={'center_x': 0.5, 'center_y': 0.5},
                               size_hint_x=None, width=200)
        screen.add_widget(username)
        return screen


DemoApp().run()
