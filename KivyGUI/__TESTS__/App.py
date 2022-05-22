#created by InfinityTM
#contact: infinitytm@pm.me
# Importing Necessary Packages

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.properties import BooleanProperty
from kivy.uix.actionbar import ActionView,ActionOverflow,ActionBar,ActionButton

# Defining the Hover Effect for the Buttons

class HoverBehavior(object):
    hovered = BooleanProperty(False)
    border_point= ObjectProperty(None)
    def __init__(self, **kwargs):
        self.register_event_type('on_enter')
        self.register_event_type('on_leave')
        Window.bind(mouse_pos=self.on_mouse_pos)
        super(HoverBehavior, self).__init__(**kwargs)

    def on_mouse_pos(self, *args):
        if not self.get_root_window():
            return
        pos = args[1]
        inside = self.collide_point(*self.to_widget(*pos))
        if self.hovered == inside:
            return
        self.border_point = pos
        self.hovered = inside
        if inside:
            self.dispatch('on_enter')
        else:
            self.dispatch('on_leave')

    def on_enter(self):
        pass

    def on_leave(self):
        pass
from kivy.factory import Factory
Factory.register('HoverBehavior', HoverBehavior)

#Creating the Title Bar

Builder.load_string("""
<TitleBar>:
    ActionBar:
        size_hint_x: None
        pos_hint: {'top':1}
        width: 600
        height: 25
        background_image: ''
        background_color: [0.95,0.95,0.95,1]
        ActionView:
            use_separator: True
            ActionPrevious:
                title: 'App Title'
                app_icon: 'logo_only.png'
                with_previous: False
                color: [ 0, 0, 0, 1]
            ActionOverflow:
            MyActionButton:
                icon: 'app_minus_hover.png' if self.hovered else "app_control_init.png"
                width: 30 if self.hovered else 30
                on_press: app.Minus_app_button()
                border: 10,10,10,10
            MyActionButton:
                icon: 'app_maxi_hover.png' if self.hovered else "app_control_init.png"
                width: 30 if self.hovered else 30
                on_press: app.MaxiMin_app_button()
                border: 10,10,10,10
            MyActionButton:
                icon: 'app_close_hover.png' if self.hovered else "app_control_init.png"
                width: 30 if self.hovered else 30
                on_press: app.close_app_button()
                border: 10,10,10,10
""")
class MyActionButton(HoverBehavior,ActionButton):
    pass
class TitleBar(FloatLayout):
    pass

# Creating your App

class MyApp(App):
    def build(self):
        Window.size=(600, 600)
        Window.clearcolor = (1, 1, 1, 1)
        b = FloatLayout()
        b.add_widget(TitleBar())

# Removing Current Bar

        Window.borderless=True
        return b
    def Minus_app_button(self):
        App.get_running_app().root_window.minimize()
    def close_app_button(self):
        app.stop()
    def MaxiMin_app_button(self):
        if Window.fullscreen:
            Window.fullscreen = False
        else:
            Window.fullscreen = True

# Running the App

if __name__=='__main__':
    app=MyApp()
    app.run()
