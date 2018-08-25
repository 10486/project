# -*- coding: utf-8 -*-

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from config import shelfs as config
import json
class Positions(BoxLayout):
    def __init__(self,*args,**kargs):
        super(Positions, self).__init__(*args,**kargs)
        self.sort = 'ip'
    def info(self,shelf):
        self.clear_widgets()
        with open('file.txt','r') as f:
            f = f.read()
            f = json.loads(f)
            asics = {str(x+1):'Нет в пуле' for x in range(config[shelf][0],config[shelf][1])}
            s = f[str(shelf)]
            for i in s:
                for k in s[i]:
                    asics[k] = i
            if(self.sort == 'ip'):
                for asic in asics:
                    self.add_widget(Asic(shelf,asic,asics[asic]))
            elif(self.sort == 'status'):
                for asic in asics:
                    if(asics[asic] != 'ACTIVE'):
                        self.add_widget(Asic(shelf,asic,asics[asic]))
                for asic in asics:
                    if(asics[asic] == 'ACTIVE'):
                        self.add_widget(Asic(shelf,asic,asics[asic]))
    def showinactive(self):
        self.clear_widgets()
        with open('file.txt','r') as f:
            f = f.read()
            f = json.loads(f)
            asics = {}
            for shelf in f:
                asics[shelf] = {str(x) for x in range(config[shelf][0],config[shelf][1]+1)}
                asics[shelf] = asics[shelf].difference(set(f[shelf]['ACTIVE']))
            for shelf in asics:
                for asic in asics[shelf]:
                    self.add_widget(Asic(shelf,asic,'Нет в пуле'))


    def selectsort(self):
        if(self.sort == 'ip'):
            self.sort = 'status'
        elif(self.sort == 'status'):
            self.sort = 'ip'

class Asic(Button):
    def __init__(self,shelf,poss,status,*args,**kargs):
        self.poss = poss
        self.shelf = shelf
        self.status = status
        super(Asic, self).__init__(*args,**kargs)
