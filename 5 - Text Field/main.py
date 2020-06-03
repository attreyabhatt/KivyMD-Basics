from kivymd.app import MDApp
from kivymd.uix.screen import Screen
import helpers
from kivy.lang import Builder


class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Green"
        screen = Screen()

        # username = MDTextField(
        #     pos_hint={'center_x': 0.5, 'center_y': 0.5},
        #     size_hint_x=None, width=200)

        username = Builder.load_string(helpers.username_input)
        screen.add_widget(username)
        return screen


DemoApp().run()
