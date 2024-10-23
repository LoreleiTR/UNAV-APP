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
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner
from kivy.clock import Clock
import pygame
import datetime

pygame.mixer.init()
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
        Label:
            text: "Login"
            font_size: 30
            size_hint_y: None
            height: 40
            pos_hint: {"center_x": 0.5, "center_y": 0.75}
        
        TextInput:
            id: email
            hint_text: "Email"
            size_hint_y: None
            height: 40
            pos_hint: {"center_x": 0.5, "center_y": 0.6}
        
        TextInput:
            id: password
            hint_text: "Password"
            password: True
            size_hint_y: None
            height: 40
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

        Button:
            text: "Login"
            size_hint_y: None
            height: 50
            pos_hint: {"center_x": 0.5, "center_y": 0.35}
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

        BoxLayout:
            padding: [30, 0, 30, 30]
            orientation: 'vertical'

            ScrollView:
                size_hint: (0.9, 0.7)
                pos_hint: {"center_x": 0.5, "center_y": 0.5}
                do_scroll_x: False
                do_scroll_y: True

                BoxLayout:
                    orientation: 'vertical'
                    size_hint_y: None
                    height: self.minimum_height

                    Label:
                        id: schedule_label
                        text: "No schedule available."
                        markup: True
                        size_hint_y: None
                        width: root.width * 0.77
                        height: self.texture_size[1]
                        halign: 'left'
                        valign: 'top'
                        text_size: self.width - 20, None
                        padding: [10, 10]

                    Widget:
                        size_hint_y: None
                        height: dp(30)

        Button:
            id: back
            size_hint: None, None
            size: dp(90), dp(60)
            pos_hint: {"x": 0.1, "y": 0.06}
            on_release:
                app.root.current = "main"
                root.manager.transition.direction = "down"
            background_normal: 'buttons/bckbtn.png'
            background_down: 'buttons/bckbtn.png'

        Button:
            id: alarm
            size_hint: None, None
            size: dp(90), dp(60)
            pos_hint: {"x": 0.5, "y": 0.06}
            text: "Set Alarm"
            on_release: root.show_alarm_popup()  # Call show_alarm_popup from the ThirdWindow
            background_normal: 'buttons/alarmbtn.png'
            background_down: 'buttons/alarmbtn.png'






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
    def __init__(self, **kwargs):
        super(ThirdWindow, self).__init__(**kwargs)
        self.schedule_file = "schedule.txt"
        self.schedule = self.load_schedule()
        self.display_schedule()

    def load_schedule(self):
        try:
            with open(self.schedule_file, 'r') as file:
                return file.readlines()
        except FileNotFoundError:
            print("Schedule file not found.")
            return []

    def display_schedule(self):
        class_times = self.extract_schedule_times(self.schedule)
        self.ids.schedule_label.text = "Class Times: " + ', '.join([time.strftime("%I:%M %p") for time in class_times])

    def extract_schedule_times(self, schedule):
        class_times = []
        days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
        
        current_day = None
        for line in schedule:
            line = line.strip()
            if line.endswith(':'):
                current_day = line[:-1].strip()
            elif current_day and line:
                self.add_class_time(line, current_day, class_times)

        return class_times

    def add_class_time(self, time_str, day, class_times):
        try:
            class_time = datetime.datetime.strptime(time_str.strip(), "%I:%M %p")
            today = datetime.datetime.now()
            weekday = today.weekday()
            days_ahead = (["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"].index(day) - weekday) % 7
            class_time += datetime.timedelta(days=days_ahead)
            class_times.append(class_time)
        except ValueError:
            print(f"Skipping invalid time format in schedule: {time_str}")

    def show_popup(self):
        content = BoxLayout(orientation='vertical')
        label = Label(text=self.ids.schedule_label.text)
        close_button = Button(text="Close")
        close_button.bind(on_press=self.close_popup)

        content.add_widget(label)
        content.add_widget(close_button)

        self.popup = Popup(title="Schedule", content=content, size_hint=(0.5, 0.5))
        self.popup.open()

    def close_popup(self, instance):
        self.popup.dismiss()



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
