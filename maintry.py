import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from kivy.lang import Builder

Window.size = (360, 640)

# Define the KV layout as a string
kv = '''
ScreenManager:
    MainScreen:
    ProfileScreen:
    SchedScreen:
    ContactScreen:
    InfoScreen:

<MainScreen>:
    name: "main"
    FloatLayout:
        Button:
            text: "Profile"
            size_hint: 0.25, 0.1
            pos_hint: {"x": 0, "y": 0}
            on_press: app.change_screen("second")

        Button:
            text: "Sched"
            size_hint: 0.25, 0.1
            pos_hint: {"x": 0.25, "y": 0}
            on_press: app.change_screen("third")

        Button:
            text: "Contact"
            size_hint: 0.25, 0.1
            pos_hint: {"x": 0.5, "y": 0}
            on_press: app.change_screen("four")

        Button:
            text: "Info"
            size_hint: 0.25, 0.1
            pos_hint: {"x": 0.75, "y": 0}
            on_press: app.change_screen("five")


<ProfileScreen>:
    name: "second"
    Label:
        text: "Welcome to Profile!"
    Button:
        text: "Go Back"
        size_hint: 0.25, 0.1
        pos_hint: {"x": 0.75, "y": 0}
        on_release:
            app.root.current = "main"
            root.manager.transition.direction = "right"

<SchedScreen>:
    name: "third"
    Label:
        text: "Welcome to Sched!"


<ContactScreen>:
    name: "four"
    Label:
        text: "Welcome to Contacts!"


<InfoScreen>:
    name: "five"
    Label:
        text: "Welcome to Info!"



        



'''


class MainScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass

class SchedScreen(Screen):
    pass

class ContactScreen(Screen):
    pass

class InfoScreen(Screen):
    pass

class ScreenManager(Screen):
    pass


class MyApp(App):
    def build(self):
        return Builder.load_string(kv)

    def change_screen(self, screen_name):
        self.root.current = screen_name


if __name__ == '__main__':
    MyApp().run()
