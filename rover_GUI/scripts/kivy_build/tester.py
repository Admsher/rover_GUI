from kivy.clock import Clock
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class WindowManager(ScreenManager):
    pass

class Window(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.current_i=0

    def update(self,*args):
        self.ids.b2.text= str(self.current_i)
        self.current_i += 1

class app(App):
    def build(self,*args):
        return Builder.load_file("/home/ninaad/catkin_ws/src/rover_GUI/scripts/kivy_build/gooey.kv")
  




if __name__=='__main__':

    app().run()