## System Imports


## Application Imports
from kivy.graphics import Ellipse, Color

from KivyGUI import utils


## Library Imports
from kivy.properties import NumericProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.widget import Widget


class RoundButton(ButtonBehavior, Widget):
    
    kv = utils.load_relative_kv(__file__)
    
    OFFSET_x = NumericProperty(15)
    OFFSET_y = NumericProperty(15)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.toggle = False
    
    def on_touch_down(self, touch):
        left = touch.x >= self.pos[0] + self.OFFSET_x / 2.0
        down = touch.y >= self.pos[1] + self.OFFSET_y / 2.0
        up = touch.y <= self.pos[1] + self.size[1] - self.OFFSET_y / 2.0
        right = touch.x <= self.pos[0] + self.size[0] - self.OFFSET_x / 2.0

        if left and down and up and right:
            self.dispatch('on_release')
            self.toggle = not self.toggle
            self.on_toggle()
    
    def on_toggle(self):
        self.canvas.clear()

        color = [1, 0, 0, 1] if self.toggle else [.3, .3, .3, 1]

        with self.canvas:
            Color(
                rgba=[1, 1, 1, .5]
            )
            Ellipse(
                size=[self.size[0] - self.OFFSET_x + 2, self.size[1] - self.OFFSET_y + 2],
                pos=[self.pos[0] + self.OFFSET_x / 2.0, self.pos[1] + self.OFFSET_y / 2.0]
            )

            Color(
                rgba=color
            )
            Ellipse(
                size=[self.size[0] - self.OFFSET_x, self.size[1] - self.OFFSET_y],
                pos=[self.pos[0] + self.OFFSET_x / 2.0 + 1, self.pos[1] + self.OFFSET_y / 2.0 + 1]
            )
