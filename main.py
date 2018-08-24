# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.uix.modalview import ModalView
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.dropdown import DropDown
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
import threading
import os
import json
import requests
import config
import time
import sys

import sub.par as par
import sub.ui
from sub.positions import Positions
from sub.shelfs import Shelfs
sys.path.append(os.path.join(sys.path[0], 'sub/'))




Config.set('graphics','resizable','0')
Config.set('graphics','width',600)
Config.set('graphics','height',500)

class HelpInfo(Label):
    def __init__(self, *arg, **karg):
        super(HelpInfo, self).__init__(*arg,**karg)
        with open('help.help','r',encoding='utf-8') as f:
            self.text = f.read()



class Help(ModalView):
    def __init__(self, *arg,**karg):
        super(Help, self).__init__()



#top menu
class Sort(Button):
    def __init__(self, *arg,**kargs):
        super(Sort, self).__init__(*arg,**kargs)
        self.text = 'Сортировка'

class Show(Button):
    def __init__(self, *arg,**kargs):
        super(Show, self).__init__(*arg)
        self.text = 'Показать неактив.'

class Reload(Button):
    def __init__(self, *arg,**kargs):
        super(Reload, self).__init__(*arg)
        self.text = 'Перезагрузка'



class HelpButton(Button):
    def __init__(self, *arg,**kargs):
        super(HelpButton, self).__init__(*arg)
        self.text = 'Помощь'

#main Layout
class Box(BoxLayout):
    pass

#main App
class MessangerApp(App):
    def __init__(self):
        super(MessangerApp,self).__init__()
        self.title = 'Асики'
    def build(self):
        # self.load = ModalView()
        self.parser = par.Parser('new.txt')
        # self.parser.loadinfo()
        self.t = threading.Thread(target=self.daemon,name='daemon')
        self.t.daemon = True
        self.t.start()
        self.box = Box()
        self.modal = Help()
        return self.box
#Переделать Функцию сравнения
    def daemon(self):
        while True:
            self.parser.loadinfo()
            with open('old.txt','r',encoding='utf-8') as old:
                with open('new.txt','r',encoding='utf-8') as new:
                    new = json.loads(new.read())
                    old = json.loads(old.read())
                    ex = []
                    for i in new:
                        dif = set(old[i]['ACTIVE']).difference(set(new[i]['ACTIVE']))
                        if(len(dif)>0):
                            ex.append([dif,i])
                            #
                            #отображение информации
                            #
            with open('new.txt','r',encoding='utf-8') as new:
                with open('old.txt','w',encoding='utf-8') as old:
                    old.write(str(new.read()))
            self.parser.clear()
            time.sleep(90)

#run
if __name__=='__main__':
    MessangerApp().run()
