from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder


class MyApp(App):

    def build(self):
         return Builder.load_string('''
Button
    text: 'Hello' if self.state == 'normal' else 'World'
''')




if __name__=='__main__':
    MyApp().run()
