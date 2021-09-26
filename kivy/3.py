from kivy.app import App
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        label = Label(text='[color=#00ff00]ICS11 is FUN![/color]',
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .5},
                      markup = True,
                      italic = True)

        return label

if __name__ == '__main__':
    app = MainApp()
    app.run()