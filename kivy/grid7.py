from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class grid(GridLayout):
    def __init__(self, **kwargs):
        super(grid,self).__init__(**kwargs)
        for i in range(24):
            b = Button(text=str(i))
            self.col = i
            self.rows = i
            self.add_widget(b)



class MyApp(App):
        def build(self):
            return grid()


app = MyApp()
app.run()