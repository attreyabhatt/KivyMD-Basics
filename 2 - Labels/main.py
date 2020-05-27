from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.font_definitions import theme_font_styles


class DemoApp(MDApp):
    def build(self):
        # halign = horizontal align

        label = MDLabel(text="Hello world", halign="center", theme_text_color="Error",
                        font_style="Subtitle2")

        # label = MDLabel(text="Hello world", halign="center",theme_text_color="Custom",
        #                 text_color=(0,0,1,1))

        # label = MDIcon(icon="language-python", halign="center")
        return label


DemoApp().run()
