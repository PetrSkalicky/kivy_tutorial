import kivy
kivy.require('1.9.0')
 
from kivy.app import App
from kivy.uix.pagelayout import PageLayout
 
class PageApp(App):
 
    def build(self):
        return PageLayout()
 
pgApp = PageApp()
 
pgApp.run()

