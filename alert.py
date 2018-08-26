import sys
import json
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.core.window import Window
class AlertApp(App):
    def __init__(self):
        super(AlertApp, self).__init__()
    def build(self):
        self.title = 'Выпали из пула'
        box = BoxLayout(orientation='vertical',size_hint_y=None)
        box.bind(minimum_height=box.setter('height'))
        info = json.loads(str(sys.stdin.read()))
        for i in info:
            for asic in i[0]:
                box.add_widget(Button(text='192.168.{}.{}'.format(i[1],asic),size_hint_y=None,height=40,color=(1,0,0,1)))
        sv = ScrollView()
        sv.add_widget(box)
        return sv
AlertApp().run()
