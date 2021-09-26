from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

sumb = ''
class MyApp(App):
    def build(self):

        test = GridLayout()

        main = StackLayout()

        kiv = Label(text='')

        def do(arg,arg2):
            global sumb
            sumb += str(arg.text)
            kiv.text = str(sumb)
        def CA(name):
            global sumb
            sumb = ''
            kiv.text = str(sumb)
        def EVAL(name):
            global sumb
            kiv.text = str(eval(sumb))


        symbs = [
            '1','2','3','**',
            '4','5','6','%',
            '7','8','9','/',
            '0','+','-','*',
        ]
        for i in symbs:
            b = Button(text = str(i), width = 100, size_hint=(None,0.15))
            main.add_widget(b)
        for i in main.children[0:]:
            i.bind(on_press = lambda x:do(x,i))

        ca = Button(text = 'CA', size_hint = (None,0.15))
        ca.bind(on_press = CA)
        ev = Button(text='=', size_hint=(None, 0.15))
        ev.bind(on_press=EVAL)
        main.add_widget(ev)
        main.add_widget(ca)
        main.add_widget(kiv)

        return main


if __name__ == '__main__':
    app = MyApp()
    app.run()