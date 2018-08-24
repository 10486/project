# -*- coding: utf-8 -*-

from kivy.uix.button import Button


class Shelf(Button):
    def __init__(self,shelf,count,*args,**kargs):
        self.count = count
        self.shelf = shelf
        super(Shelf, self).__init__(*args,**kargs)
        self.text = 'Полка:{}   Кол-во:{}'.format(self.shelf,self.count)
