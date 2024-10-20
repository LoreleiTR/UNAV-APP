from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.image import Image

# Map 
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.mapview import MapView, MapMarker
from kivy.graphics import Rectangle

Window.size = (360, 640)

# Define the KV layout as a string
kv = '''
WindowManager:
    MainWindow:
    SecondWindow:
    ThirdWindow:
    FourthWindow:
    FifthWindow:

<MainWindow>:
    name: "main"

    # Use FloatLayout to allow buttons to float over the MapView
    FloatLayout:
        # Full-screen MapView
        MapView:
            size_hint: 1, 1  # Map fills the entire screen
            lat: 37.7749  # Center latitude (San Francisco)
            lon: -122.4194  # Center longitude (San Francisco)
            zoom: 10
            MapMarker:
                lat: 37.7749
                lon: -122.4194

        # Floating buttons aligned at the bottom of the screen
        Button:
            id: "Profile"
            size_hint: None, None
            size: dp(90), dp(60)
            pos_hint: {"x": 0, "y": 0}  # Aligned at the bottom-left
            on_release:
                app.root.current = "second"
                root.manager.transition.direction = "right"
            # Add an image as the button's background
            background_normal: 'buttons\profilebtn.png'  # Path to your image
            background_down: 'buttons\profilebtn.png'  # Path for pressed state (optional)
        

        Button:
            id: "Sched"
            size_hint: None, None
            size: dp(90), dp(60)
            pos_hint: {"x": 0.25, "y": 0}  # Positioned next to Profile
            on_release:
                app.root.current = "third"
                root.manager.transition.direction = "right"
            # Add an image as the button's background
            background_normal: 'buttons\datebtn.png'  # Path to your image
            background_down: 'buttons\datebtn.png'  # Path for pressed state (optional)

        Button:
            id: "Contact"
            size_hint: None, None
            size: dp(90), dp(60)
            pos_hint: {"x": 0.5, "y": 0}  # Positioned next to Sched
            on_release:
                app.root.current = "fourth"
                root.manager.transition.direction = "right"
            # Add an image as the button's background
            background_normal: 'buttons\callbtn.png'  # Path to your image
            background_down: 'buttons\callbtn.png'  # Path for pressed state (optional)


        Button:
            id: "Info"
            size_hint: None, None
            size: dp(90), dp(60)
            pos_hint: {"x": 0.75, "y": 0}  # Positioned next to Contact
            on_release:
                app.root.current = "five"
                root.manager.transition.direction = "right"
            background_normal: 'buttons\infobtn.png'  # Path to your image
            background_down: 'buttons\infobtn.png'  # Path for pressed state (optional)


<SecondWindow>:
    name: "second"

    Button:
        text: "Go Back"
        size_hint: 0.25, 0.1
        pos_hint: {"x": 0, "y": 0}
        on_release:
            app.root.current = "main"
            root.manager.transition.direction = "right"


<ThirdWindow>:
    name: "third"

    Button:
        text: "Go Back"
        size_hint: 0.25, 0.1
        pos_hint: {"x": 0, "y": 0}
        on_release:
            app.root.current = "main"
            root.manager.transition.direction = "right"

<FourthWindow>:
    name: "fourth"

    Button:
        text: "Go Back"
        size_hint: 0.25, 0.1
        pos_hint: {"x": 0, "y": 0}
        on_release:
            app.root.current = "main"
            root.manager.transition.direction = "right"

<FifthWindow>:
    name: "five"

    Button:
        text: "Go Back"
        size_hint: 0.25, 0.1
        pos_hint: {"x": 0, "y": 0}
        on_release:
            app.root.current = "main"
            root.manager.transition.direction = "right"
'''

# Define the Screen classes
class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    pass

class ThirdWindow(Screen):
    pass

class FourthWindow(Screen):
    pass

class FifthWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

# Define the main app
class MyMainApp(App):
    def build(self):
        return Builder.load_string(kv)  # Load the KV layout from the string

if __name__ == "__main__":
    MyMainApp().run()
