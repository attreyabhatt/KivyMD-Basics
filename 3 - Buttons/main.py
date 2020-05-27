from kivymd.app import MDApp
from kivymd.uix.button import MDFloatingActionButton, MDFlatButton
from kivymd.uix.screen import Screen


class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        btn1 = MDFlatButton(text='Hello World', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        btn = MDFloatingActionButton(icon="android",
                                     pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                     )
        screen.add_widget(btn1)
        return screen


DemoApp().run()
