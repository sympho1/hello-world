import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.button import Button

class ITCApp(App):
    def build(self):
        return Button(text='Hello kivy !')


if __name__ == '__main__':
    ITCApp().run()