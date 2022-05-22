from kivy.app import App
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image

kv = """
<RoundButton>:
    
    canvas:
        Color:
            rgba: 1, 0, 0, 1
        Ellipse:
            size:
                [self.size[0] - root.OFFSET_x,
                self.size[1] - root.OFFSET_y]
            pos:
                [self.pos[0] + root.OFFSET_x / 2.0,
                self.pos[1] + root.OFFSET_y / 2.0]
    
BoxLayout:
    Button:
    RoundButton:
        source: 'image.png'
        on_release: print('Release event!')
"""


class RoundButton(ButtonBehavior, Image):
    OFFSET_x = NumericProperty(100)
    OFFSET_y = NumericProperty(200)

    def on_touch_down(self, touch):
        left = touch.x >= self.pos[0] + self.OFFSET_x / 2.0
        down = touch.y >= self.pos[1] + self.OFFSET_y / 2.0
        up = touch.y <= self.pos[1] + self.size[1] - self.OFFSET_y / 2.0
        right = touch.x <= self.pos[0] + self.size[0] - self.OFFSET_x / 2.0

        if left and down and up and right:
            print('collided!')
            self.dispatch('on_release')
        else:
            print('outside of area!')


class TestApp(App):
    def build(self):
        return Builder.load_string(kv)


if __name__ == '__main__':
    TestApp().run()
