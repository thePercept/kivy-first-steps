from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder


class MyApp(App):

    def build(self):
         return Builder.load_string('''
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
ScreenManager
    id: sm
    transition: FadeTransition()
    Screen
        name : 'sc1'
        Button 
            text: 'goto 2'
            background_color: 1,0,1,1
            on_release: sm.current = 'sc2'
    Screen 
        name : 'sc2'
        Button 
            text:  'goto 1'
            on_release: sm.current = 'sc1'        
''')







if __name__=='__main__':
    MyApp().run()
