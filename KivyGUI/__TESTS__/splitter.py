import kivy
kivy.require('1.8.1')

from kivy.app import App
from kivy.lang import Builder

root = Builder.load_string('''
BoxLayout:
    orientation: 'vertical'
    Splitter:
        sizable_from: 'top'
        Button:
            text: 'something2'

''')


class TestApp(App):
    def build(self):
        return root


if __name__ == '__main__':
    TestApp().run()
