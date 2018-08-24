# -*- coding: utf-8 -*-

from kivy.uix.boxlayout import BoxLayout
from sub.shelf import Shelf
import json
class Shelfs(BoxLayout):
    def __init__(self,*args,**kargs):
        super(Shelfs, self).__init__(*args,**kargs)
        self.info()

    def info(self):
        self.clear_widgets()
        with open('file.txt','r') as f:
            f = f.read()
            f = json.loads(f)
            shelfs = {str(x+1):0 for x in range(26)}
            for i in f:
                shelfs[i] = len(f[i]['ACTIVE'])
        for i in shelfs:
            if(shelfs[i] != 0):
                self.add_widget(Shelf(i,shelfs[i]))
