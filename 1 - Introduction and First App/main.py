from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class DemoApp(MDApp):
    def build(self):
        # halign = horizontal align
        label = MDLabel(text="Hello world", halign="center")
        return label


DemoApp().run()
