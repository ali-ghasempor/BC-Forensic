import kivy
kivy.require('1.0.7')

from kivy.app import App
from kivy.uix.button import Button

class Testapp (App):
    def build(self):
        return Button(text='hello')
if __name__ == '__main__':
    Testapp().run()