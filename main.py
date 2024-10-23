from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.image import Image
import webbrowser
from kivy.garden.mapview import MapView
import json
import os
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

# Set the window size
Window.size = (360, 640)

# Define the KV layout as a string
kv = '''
WindowManager:
    LoginScreen:
    MainWindow:
    SecondWindow:
    ThirdWindow:
    FourthWindow:
    FifthWindow:

<LoginScreen>:
    name: "login"
    
    FloatLayout:
        Image:
            source: 'bg\loginbg.png'
            allow_stretch: True
            keep_ratio: False
            size_hint: (1, 1)
            pos_hint: {"x": 0, "y": 0}
        Label:
            text: "LOGIN"
            font_size: 40
            bold: True
            size_hint: (0.4, 0.1)  # Adjust size for better fit
            pos_hint: {"center_x": 0.5, "center_y": 0.7}  # Center in the red box area
        
        TextInput:
            id: email
            hint_text: "Email"
            size_hint: (0.8, None)  # Control width relative to red box
            height: 50  # Adjust height for better spacing
            pos_hint: {"center_x": 0.5, "center_y": 0.57}  # Position closer to the label
        
        TextInput:
            id: password
            hint_text: "Password"
            password: True
            size_hint: (0.8, None)  # Control width relative to red box
            height: 50
            pos_hint: {"center_x": 0.5, "center_y": 0.47}  # Keep distance consistent with the email field

        Button:
            text: "Login"
            size_hint: (0.6, None)  # Control width to match other inputs
            height: 50
            pos_hint: {"center_x": 0.5, "center_y": 0.35}  # Align with text inputs
            on_release: root.verify_login()


<MainWindow>:
    name: "main"
    FloatLayout:
        MapView:
            size_hint: 1, 1
            lat: 37.7749
            lon: -122.4194
            zoom: 10
            MapMarker:
                lat: 37.7749
                lon: -122.4194
        Button:
            id: "Profile"
            size_hint: None, None
            size: dp(90), dp(60)
            pos_hint: {"x": 0, "y": 0}
            on_release:
                app.root.current = "second"
                root.manager.transition.direction = "up"
            background_normal: 'buttons/profilebtn.png'
            background_down: 'buttons/profilebtn.png'
        Button:
            id: "Sched"
            size_hint: None, None
            size: dp(90), dp(60)
            pos_hint: {"x": 0.25, "y": 0}
            on_release:
                app.root.current = "third"
                root.manager.transition.direction = "up"
            background_normal: 'buttons/datebtn.png'
            background_down: 'buttons/datebtn.png'
        Button:
            id: "Contact"
            size_hint: None, None
            size: dp(90), dp(60)
            pos_hint: {"x": 0.5, "y": 0}
            on_release:
                app.root.current = "fourth"
                root.manager.transition.direction = "up"
            background_normal: 'buttons/callbtn.png'
            background_down: 'buttons/callbtn.png'
        Button:
            id: "Info"
            size_hint: None, None
            size: dp(90), dp(60)
            pos_hint: {"x": 0.75, "y": 0}
            on_release:
                app.root.current = "five"
                root.manager.transition.direction = "up"
            background_normal: 'buttons/infobtn.png'
            background_down: 'buttons/infobtn.png'

<SecondWindow>:
    name: "second"
    FloatLayout:
        Image:
            source: 'bg\profilebg.png'
            allow_stretch: True
            keep_ratio: False
            size_hint: (1, 1)
            pos_hint: {"x": 0, "y": 0}

        Image:
            id: profile_pic
            source: ''  # User profile picture
            size_hint: None, None
            size: dp(100), dp(100)
            pos_hint: {"center_x": 0.5, "center_y": 0.7}
        
        Label:
            id: name
            text: "NAME: [u]{}[/u]"
            markup: True
            font_size: 18
            size_hint: None, None
            size: 200, 40
            pos_hint: {"center_x": 0.5, "center_y": 0.54}
            halign: 'left'
            valign: 'middle'
            text_size: self.size

        Label:
            id: section
            text: "SECTION: [u]{}[/u]"
            markup: True
            font_size: 18
            size_hint: None, None
            size: 200, 40
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'left'
            valign: 'middle'
            text_size: self.size

        Label:
            id: sr_number
            text: "SR Number: [u]{}[/u]"
            markup: True
            font_size: 18
            size_hint: None, None
            size: 200, 40
            pos_hint: {"center_x": 0.5, "center_y": 0.46}
            halign: 'left'
            valign: 'middle'
            text_size: self.size

        Button:
            id: "Go to BSU Account"
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {"center_x": 0.5, "center_y": 0.3}
            on_release: app.open_bsu_account()
            background_normal: 'buttons/bsuaccbtn.png'
            background_down: 'buttons/bsuaccbtn.png'
        
        Button:
            id: back
            size_hint: None, None
            size: dp(90), dp(60)
            pos_hint: {"x": 0.375, "y": 0.06}
            on_release:
                app.root.current = "main"
                root.manager.transition.direction = "down"
            background_normal: 'buttons/bckbtn.png'
            background_down: 'buttons/bckbtn.png'



<ThirdWindow>:
    name: "third"
    FloatLayout:
        Image:
            source: 'bg/schedbg.png'
            allow_stretch: True
            keep_ratio: False
            size_hint: (1, 1)
            pos_hint: {"x": 0, "y": 0}

        # Red box 
        BoxLayout:
            padding: [30, 0, 30, 30]  # Add space (left, top, right, bottom)
            
            ScrollView:
                size_hint: (0.9, 0.7)  # Match the adjusted size
                pos_hint: {"center_x": 0.5, "center_y": 0.5}  # Center within the parent layout
                do_scroll_x: False  # Disable horizontal scrolling
                do_scroll_y: True  # Enable vertical scrolling

                BoxLayout:
                    orientation: 'vertical'
                    size_hint_y: None  # Allow vertical resizing
                    height: self.minimum_height  # Set height to fit all children

                    Label:
                        id: schedule_label
                        text: "No schedule available."
                        markup: True  # Enable markup
                        size_hint_y: None  # Let the height adjust based on content
                        size_hint_x: None  # Remove automatic width scaling
                        width: root.width * 0.77  # Make the label slightly smaller than the red box
                        height: self.texture_size[1]  # Adjust height dynamically based on text
                        halign: 'left'  # Align text to the left
                        valign: 'top'  # Align text to the top
                        text_size: self.width - 20, None  # Allow text to wrap within the label's width
                        padding: [10, 10]  # Add padding for better visuals

                    # Spacer at the bottom for extra space after scrolling
                    Widget:
                        size_hint_y: None
                        height: dp(30)  # Add space at the bottom

      
        Button:
            id: back
            size_hint: None, None
            size: dp(90), dp(60)
            pos_hint: {"x": 0.375, "y": 0.06}
            on_release:
                app.root.current = "main"
                root.manager.transition.direction = "down"
            background_normal: 'buttons/bckbtn.png'
            background_down: 'buttons/bckbtn.png'





<FourthWindow>:
    name: "fourth"
    FloatLayout:
        Image:
            source: 'bg/contbg.png'
            allow_stretch: True
            keep_ratio: False
            size_hint: (1, 1)
            pos_hint: {"x": 0, "y": 0}
        Button:
            id: back
            size_hint: None, None
            size: dp(90), dp(60)
            pos_hint: {"x": 0.375, "y": 0.06}
            on_release:
                app.root.current = "main"
                root.manager.transition.direction = "down"
            background_normal: 'buttons/bckbtn.png'
            background_down: 'buttons/bckbtn.png'
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
        Image:
            source: 'bg/Abtinfo.png'
            allow_stretch: True
            keep_ratio: False
            size_hint: (1, 1)
            pos_hint: {"x": 0, "y": 0}
        Button:
            id: back
            size_hint: None, None
            size: dp(90), dp(60)
            pos_hint: {"x": 0.375, "y": 0.06}
            on_release:
                app.root.current = "main"
                root.manager.transition.direction = "down"
            background_normal: 'buttons/bckbtn.png'
            background_down: 'buttons/bckbtn.png'
'''

# Load users from the text file and convert to dictionary format

def load_users():
    users = {}
    if os.path.exists('users.txt'):
        with open('users.txt', 'r') as f:
            for line in f:
                email, password, schedule, image_path, name, section, sr_number, bsu_url = line.strip().split(',')
                users[email.upper()] = {
                    "password": password, 
                    "schedule": schedule,
                    "image_path": image_path,
                    "name": name,
                    "section": section,
                    "sr_number": sr_number,
                    "bsu_url": bsu_url
                }
    return users


# Save users to the JSON file (in case you need to add new users)
def save_users(users):
    with open('users.txt', 'w') as f:
        for email, data in users.items():
            f.write(f"{email},{data['password']},{data['schedule']}\n")

# Load users at the start
users = load_users()

class LoginScreen(Screen):
    def verify_login(self):
        email = self.ids.email.text.upper()
        password = self.ids.password.text

        # Check if the user exists and password matches
        if email in users and users[email]["password"] == password:
            # Successful login, go to the main screen
            app = App.get_running_app()
            app.current_user = email
            app.root.current = "main"
        else:
            # Incorrect login
            print("Invalid credentials, please try again.")
            self.ids.email.text = ""
            self.ids.password.text = ""

class MainWindow(Screen):
    pass

class SecondWindow(Screen):
    def on_enter(self):
        app = App.get_running_app()
        user = app.current_user
        if user:
            user_data = users[user]
            # Update the profile picture, SR number, and set the BSU account URL
            self.ids.profile_pic.source = user_data["image_path"]
            self.ids.name.text = f"NAME: {user_data['name']}"
            self.ids.section.text = f"SECTION: {user_data['section']}"
            self.ids.sr_number.text = f"SR NUMBER: {user_data['sr_number']}"
            app.bsu_account_url = user_data["bsu_url"]



class ThirdWindow(Screen):
    def on_enter(self):
        app = App.get_running_app()
        user = app.current_user
        if user:
            schedule_file = users[user]["schedule"]  # Get the filename
            schedule_text = "No schedule available."
            
            if os.path.exists(schedule_file):
                with open(schedule_file, 'r') as f:
                    schedule = f.read().strip()  # Read the content of the schedule file

                # Apply markup for bold and underline the days, and bold the times
                if schedule:
                    schedule_text = "WEEKLY SCHEDULE:\n\n"
                    schedule = schedule.replace("MONDAY:", "[b][u]MONDAY:[/u][/b]")
                    schedule = schedule.replace("TUESDAY:", "[b][u]TUESDAY:[/u][/b]")
                    schedule = schedule.replace("WEDNESDAY:", "[b][u]WEDNESDAY:[/u][/b]")
                    schedule = schedule.replace("THURSDAY:", "[b][u]THURSDAY:[/u][/b]")
                    schedule = schedule.replace("FRIDAY:", "[b][u]FRIDAY:[/u][/b]")
                    schedule = schedule.replace("SATURDAY:", "[b][u]SATURDAY:[/u][/b]")
                    schedule = schedule.replace("SUNDAY:", "[b][u]SUNDAY:[/u][/b]")

                    # Bold the times (assumes times follow this format)
                    schedule = schedule.replace("AM", "[b]AM[/b]").replace("PM", "[b]PM[/b]")
                    
                    schedule_text += schedule
            
            # Assign the processed text with markup to the label
            self.ids.schedule_label.text = schedule_text
            self.ids.schedule_label.markup = True  # Enable markup for the label


class FourthWindow(Screen):
    pass

class FifthWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

# Define the main app
class MyMainApp(App):
    current_user = None
    bsu_account_url = ""

    def build(self):
        return Builder.load_string(kv)  # Load the KV layout from the string

    def open_website(self, url):
        webbrowser.open(url)
    def open_bsu_account(self):
        if self.bsu_account_url:
            webbrowser.open(self.bsu_account_url)

if __name__ == "__main__":
    MyMainApp().run()
