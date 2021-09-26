from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window


class screen(GridLayout):
    Window.size = (700,500)
    def __init__(self, **kwargs):
        super(screen,self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text = 'Username'))
        self.username = TextInput(multiline = False)
        self.add_widget(self.username)
        self.row = 2
        self.add_widget(Label(text='Password'))
        self.password = TextInput(multiline=False)
        self.add_widget(self.password)
        self.row = 3
        self.col_default_width = 2
        self.enter = Button(text = 'Enter')
        #self.enter.bind(on_press = call)
        self.add_widget(self.enter)




class MyApp(App):
    def build(self):

        return screen()


if __name__ == '__main__':
    app = MyApp()
    app.run()