from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line


class Marker(Widget):
    def on_touch_down(self, touch):
        super(Marker,self).on_touch_down(touch)
        with self.canvas:
            self.line = Line(points=[touch.pos[0], touch.pos[1]],width = 2)
    def on_touch_move(self, touch):
        self.line.points = self.line.points + [touch.pos[0], touch.pos[1]]
class makedo(App):
    def build(self):
        win = Marker()
        return win


makedo().run()