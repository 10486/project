from kivy.uix.boxlayout import BoxLayout
from shelf import Shelf
class Shelfs(BoxLayout):
    def __init__(self,*args,**kargs):
        super(Shelfs, self).__init__(*args,**kargs)
        with open('file.txt','r') as f:
            f = f.readlines()
            shelfs = {str(x+1):0 for x in range(26)}
            for i in f:
                i = i.split(';')
                shelfs[i[0][2:]]+=1
            for i in shelfs:
                if(shelfs[i] != 0):
                    self.add_widget(Shelf(i,shelfs[i]))
            def info(arg):
                print(arg)
