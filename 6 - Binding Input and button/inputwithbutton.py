from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder
import helpers


class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        screen = Screen()

        self.username = Builder.load_string(helpers.username_input)
        button = MDRectangleFlatButton(text='Show',
                                       pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                       on_release=self.show_data)
        screen.add_widget(self.username)
        screen.add_widget(button)
        return screen

    def show_data(self,obj):
        print(self.username.text)


DemoApp().run()
