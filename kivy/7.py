from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

sumb = 0
class MyApp(App):
    def build(self):



        main = StackLayout()

        kiv = Label(text='')

        def do(arg,arg2):
            global sumb
            sumb += int(arg.text)
            kiv.text = str(sumb)

        for i in range(24):
            b = Button(text = str(i), width = 100, size_hint=(None,0.15))
            main.add_widget(b)
        for i in main.children[0:]:
            i.bind(on_press = lambda x:do(x,i))


        main.add_widget(kiv)

        return main


if __name__ == '__main__':
    app = MyApp()
    app.run()