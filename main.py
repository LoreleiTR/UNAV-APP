from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.image import Image
import webbrowser

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
                root.manager.transition.direction = "up"
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
                root.manager.transition.direction = "up"
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
                root.manager.transition.direction = "up"
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
                root.manager.transition.direction = "up"
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

    FloatLayout:
    # Fullscreen background image (acts as wallpaper)
    Image:
        source: 'bg\contbg.png'
        allow_stretch: True  # Allow the image to stretch to fill the screen
        keep_ratio: False  # Disable keeping the aspect ratio, so it covers the screen fully
        size_hint: (1, 1)  # Make the image fill the whole screen
        pos_hint: {"x": 0, "y": 0}  # Align to the bottom left

    Button:
        id:back
        size_hint: None, None
        size: dp(90), dp(60)
        pos_hint: {"x":  0.375, "y": 0.06}
        on_release:
            app.root.current = "main"
            root.manager.transition.direction = "down"
        background_normal: 'buttons/bckbtn.png'  # Path to your image
        background_down: 'buttons/bckbtn.png'  # Path for pressed state (optional)
        
    Button:
        
        size_hint: None, None
        size: dp(90), dp(60)
        pos_hint: {"x": 0.375, "y": 0.72}
        on_release: app.open_website('https://batstateu.edu.ph/?fbclid=IwY2xjawGDScZleHRuA2FlbQIxMAABHStZ27tFxqOOwy0CACeJt8NRt1LKx5NyGZBbDR8bfwEfVh0Rlqy5xISIMQ_aem_TBzMYBpi8PKAErWOlBWgkA')
        background_normal: 'buttons/webbtn.png'  
        background_down: 'buttons/webbtn.png'  



    Button:
        
        size_hint: None, None
        size: dp(90), dp(60)
        pos_hint: {"x": 0.375, "y": 0.53}
        on_release: app.open_website('https://www.facebook.com/BatStateUTheNEU')
        background_normal: 'buttons/fbbtn.png'  
        background_down: 'buttons/fbbtn.png'  

    Button:
        
        size_hint: None, None
        size: dp(90), dp(60)
        pos_hint: {"x": 0.375, "y": 0.32}
        on_release: app.open_website('https://www.youtube.com/@batstateutheneu')
        background_normal: 'buttons/ytbtn.png'
        background_down: 'buttons/ytbtn.png'  

    

<FifthWindow>:
    name: "five"

    FloatLayout:
    # Fullscreen background image (acts as wallpaper)
    Image:
        source: 'bg\Abtinfo.png'
        allow_stretch: True  # Allow the image to stretch to fill the screen
        keep_ratio: False  # Disable keeping the aspect ratio, so it covers the screen fully
        size_hint: (1, 1)  # Make the image fill the whole screen
        pos_hint: {"x": 0, "y": 0}  # Align to the bottom left


    Button:
        id:back
        size_hint: None, None
        size: dp(90), dp(60)
        pos_hint: {"x":  0.375, "y": 0.06}
        on_release:
            app.root.current = "main"
            root.manager.transition.direction = "down"
        background_normal: 'buttons/bckbtn.png'  # Path to your image
        background_down: 'buttons/bckbtn.png'  # Path for pressed state (optional)
    
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
    

    def open_website(self, url):
        webbrowser.open(url)


if __name__ == "__main__":
    MyMainApp().run()
