from kivy.app import App
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_string('''
#:import random random.random
#:import SlideTransition kivy.uix.screenmanager.SlideTransition
#:import SwapTransition kivy.uix.screenmanager.SwapTransition
#:import WipeTransition kivy.uix.screenmanager.WipeTransition
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
<CustomScreen>:
    hue: random()
    canvas:
        Color:
            hsv: self.hue, .5, .3
        Rectangle:
            size: self.size

    Label:
        font_size: 42
        text: root.name

    Button:
        text: 'Next screen'
        size_hint: None, None
        pos_hint: {'right': 1}
        size: 150, 50
        on_release: root.manager.current = root.manager.next()

    Button:
        text: 'Previous screen'
        size_hint: None, None
        size: 150, 50
        on_release: root.manager.current = root.manager.previous()

    BoxLayout:
        size_hint: .5, None
        height: 250
        pos_hint: {'center_x': .5}
        orientation: 'vertical'

        Button:
            text: 'Use SlideTransition with "up" direction'
            on_release: root.manager.transition = SlideTransition(direction="up")

        Button:
            text: 'Use SlideTransition with "down" direction'
            on_release: root.manager.transition = SlideTransition(direction="down")

        Button:
            text: 'Use SlideTransition with "left" direction'
            on_release: root.manager.transition = SlideTransition(direction="left")

        Button:
            text: 'Use SlideTransition with "right" direction'
            on_release: root.manager.transition = SlideTransition(direction="right")

        Button:
            text: 'Use SwapTransition'
            on_release: root.manager.transition = SwapTransition()

        Button:
            text: 'Use WipeTransition'
            on_release: root.manager.transition = WipeTransition()

        Button:
            text: 'Use FadeTransition'
            on_release: root.manager.transition = FadeTransition()
''')

class CustomScreen(Screen):
    hue = NumericProperty(0)

class ScreenManagerApp(App):

    def build(self):
        root = ScreenManager()
        for x in range(4):
            root.add_widget(CustomScreen(name='Screen %d' % x))
        box = BoxLayout(orientation='vertical')
        box.add_widget(Button(text='hello world'))
        box.add_widget(root)
        return box

if __name__ == '__main__':
    ScreenManagerApp().run()
