from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import config
class Positions(BoxLayout):
    def __init__(self,*args,**kargs):
        super(Positions, self).__init__(*args,**kargs)
    def info(self,shelf):
        self.clear_widgets()
        with open('file.txt','r') as f:
            f = f.readlines()
            asics = {str(x+1):'Not found' for x in range(2,config.shelfs[shelf])}
            for i in f:
                i = i.split(';')
                if(i[0][2:] == str(shelf)):
                    asics[i[1][2:]] = i[2][2:-1]
            for asic in asics:

                self.add_widget(Asic(shelf,asic,asics[asic]))

class Asic(Button):
    def __init__(self,shelf,poss,status,*args,**kargs):
        self.poss = poss
        self.shelf = shelf
        self.status = status
        super(Asic, self).__init__(*args,**kargs)
