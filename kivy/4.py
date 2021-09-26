from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
class MyApp(App):
    def build(self):

        def runf(i):
            pass
        btn = Button(text = 'ICS11 IS FUN!')
        btn.bind(on_press = runf)
        return btn
if __name__ == '__main__':
    app = MyApp()
    app.run()