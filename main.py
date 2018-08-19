from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.dropdown import DropDown
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
import sys
import threading
import os
import json
import requests
import config
import time

import par
import ui
from positions import Positions
from shelfs import Shelfs
sys.path.append(os.path.join(sys.path[0], 'sub/'))




Config.set('graphics','resizable','0')
Config.set('graphics','width',600)
Config.set('graphics','height',500)





#top menu
class ViewButton(Button):
    def __init__(self, *arg,**kargs):
        super(ViewButton, self).__init__(*arg,**kargs)
        self.text = 'View'


class FileButton(Button):
    def __init__(self, *arg,**kargs):
        super(FileButton, self).__init__(*arg)


class HelpButton(Button):
    def __init__(self, *arg,**kargs):
        super(HelpButton, self).__init__(*arg)
        self.text = 'Help'






class EditButton(Button):
    def __init__(self, *arg,**karg):
        super(EditButton, self).__init__(*arg,**karg)
        self.text = 'Edit'
    # def on_press(self):
    #     proc = subprocess.run("python addPost.py", shell=True, stdout=subprocess.PIPE)


class DropDowen(DropDown):
    def __init__(self, *arg,**karg):
        super(DropDowen, self).__init__()








#main Layout
class Box(BoxLayout):
    pass

#main App
class MessangerApp(App):
    def __init__(self):
        super(MessangerApp,self).__init__()
        self.title = 'Асики'
    def build(self):
        self.parser = par.Parser('new.txt')
        self.t = threading.Thread(target=self.daemon,name='daemon')
        self.t.daemon = True
        self.t.start()
        self.box = Box()
        return self.box

    def daemon(self):
        while True:
            self.parser.loadinfo()
            with open('old.txt','r',encoding='utf-8') as old:
                with open('new.txt','r',encoding='utf-8') as new:
                    new = new.readlines()
                    old = old.readlines()
                    exeption = []
                    for i,item in enumerate(old):
                        if (new[i] != item):
                            exeption.append([item,new[i]])
                            #
                            #отображение информации
                            #
            with open('new.txt','r',encoding='utf-8') as new:
                with open('old.txt','r',encoding='utf-8') as old:
                    old.write(new.read)
            print(exeption)
            self.parser.clear()
            time.sleep(1800)



#run
if __name__=='__main__':
    MessangerApp().run()
