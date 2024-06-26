from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.app import App
from plyer import filechooser

import pyqrcode as qr

Builder.load_file('querrecode.kv')

class MLayout(Widget):
    
    def on_selection(self, selection):
        if selection:
            global s
            s = selection[0]
        print(s)
    def gino(self):
        filechooser.choose_dir(on_selection= self.on_selection)
        url = self.ids.intext.text
        nome = self.ids.inname.text
        scala = self.ids.insacala.text
        sfondo = self.ids.sfondo2.hex_color
        interno = self.ids.interno2.hex_color
        
        if sfondo and interno == '#ffffffff':
            interno = '#00000000'
        img = qr.create(url)
        img.png(f'{s}\{nome}.png', scale= scala, module_color= interno[:-2], background = sfondo[:-2])

class MyApp(App):
    def build(self):
        return MLayout()

if __name__=="__main__":
    MyApp().run()