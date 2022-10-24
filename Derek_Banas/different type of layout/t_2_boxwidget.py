import kivy
kivy.require('1.9.0')
 
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
 
class BoxApp(App):
 
    def build(self):
        return BoxLayout()
 
bxApp = BoxApp()
 
bxApp.run()




