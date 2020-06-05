from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp


class DemoApp(MDApp):

    def build(self):
        screen = Screen()
        data_table = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                 size_hint=(0.9, 0.6),
                                 check=True,
                                 rows_num=10,
                                 column_data=[
                                     ("No.", dp(18)),
                                     ("Food", dp(20)),
                                     ("Calories", dp(20))
                                 ],
                                 row_data=[
                                     ("1", "Burger", "300"),
                                     ("2", "Oats", "200"),
                                     ("3", "Oats", "200"),
                                     ("4", "Oats", "200"),
                                     ("5", "Oats", "200"),
                                     ("6", "Oats", "200"),
                                     ("7", "Oats", "200"),
                                     ("8", "Oats", "200")

                                 ]
                                 )
        data_table.bind(on_row_press=self.on_row_press)
        data_table.bind(on_check_press=self.on_check_press)
        screen.add_widget(data_table)
        return screen

    def on_row_press(self, instance_table, instance_row):
        print(instance_table, instance_row)

    def on_check_press(self, instance_table, current_row):
        print(instance_table, current_row)


DemoApp().run()
