from kivy.uix.boxlayout import BoxLayout
import threading
import json
import requests
class Main(BoxLayout):

    def __init__(self, *args,**arg):
        super(Main, self).__init__(*args,**arg)
        self.id = 'Main'


    
