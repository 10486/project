# -*- coding: utf-8 -*-

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
# import config
import json
class Positions(BoxLayout):
    def __init__(self,*args,**kargs):
        super(Positions, self).__init__(*args,**kargs)
    def info(self,shelf):
        self.clear_widgets()
        with open('file.txt','r') as f:
            f = f.read()
            f = json.loads(f)
            asics = {str(x+1):'Нет в пуле' for x in range(2,40)}
            s = f[str(shelf)]
            for i in s:
                for k in s[i]:
                    asics[k] = i
            for asic in asics:
                self.add_widget(Asic(shelf,asic,asics[asic]))

class Asic(Button):
    def __init__(self,shelf,poss,status,*args,**kargs):
        self.poss = poss
        self.shelf = shelf
        self.status = status
        super(Asic, self).__init__(*args,**kargs)
