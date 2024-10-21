import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.spinner import Spinner
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.clock import Clock
import time

kivy.require('2.1.0')  # Ensure the correct version of Kivy

# Hardcoded users
users = {
    'lei@gmail.com': {'password': '123', 'schedule': {'Mon': 'jog (7AM - 8AM)', 'Tue': 'sleep (7AM - 8AM)'}},
    'lore@gmail.com': {'password': '456', 'schedule': {'Mon': 'sleep (7AM - 8AM)', 'Tue': 'jog (7AM - 8AM)'}}
}

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        
        self.email_input = TextInput(hint_text="Email", size_hint=(None, None), height=40, width=200)
        self.password_input = TextInput(hint_text="Password", password=True, size_hint=(None, None), height=40, width=200)
        self.login_button = Button(text="Login", size_hint=(None, None), height=50, width=200)
        self.login_button.bind(on_press=self.login)

        self.layout.add_widget(self.email_input)
        self.layout.add_widget(self.password_input)
        self.layout.add_widget(self.login_button)
        self.add_widget(self.layout)

    def login(self, instance):
        email = self.email_input.text
        password = self.password_input.text

        if email in users and users[email]['password'] == password:
            self.manager.current = 'schedule'
            self.manager.get_screen('schedule').update_schedule(email)
        else:
            self.show_popup("Login Failed", "Incorrect email or password.")

    def show_popup(self, title, message):
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text=message))
        close_button = Button(text="Close", size_hint=(None, None), width=200, height=50)
        content.add_widget(close_button)
        popup = Popup(title=title, content=content, size_hint=(None, None), size=(400, 200))
        close_button.bind(on_press=popup.dismiss)
        popup.open()


class ScheduleScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')

        # Initialize the schedule_label here, so it's only added once
        self.schedule_label = Label(text="Schedule will appear here.")
        self.layout.add_widget(self.schedule_label)

        # Spinner and button for alarm
        self.alarm_spinner = Spinner(text="Set Alarm", values=("5 mins", "10 mins", "None"), size_hint=(None, None), width=200)
        self.alarm_button = Button(text="Set Alarm", size_hint=(None, None), height=50, width=200)

        self.layout.add_widget(self.alarm_spinner)
        self.layout.add_widget(self.alarm_button)
        
        # Bind the button to the set_alarm method
        self.alarm_button.bind(on_press=self.set_alarm)

        # Add the layout to the screen
        self.add_widget(self.layout)

    def update_schedule(self, email):
        # Update the schedule based on the logged-in user
        user_schedule = users[email]['schedule']
        schedule_text = "\n".join([f"{day}: {activity}" for day, activity in user_schedule.items()])
        self.schedule_label.text = f"Your Schedule:\n{schedule_text}"

    def set_alarm(self, instance):
        alarm_time = self.alarm_spinner.text
        if alarm_time == "None":
            self.show_popup("No Alarm", "No alarm will be set.")
        else:
            minutes_before = int(alarm_time.split()[0])
            self.show_popup("Alarm Set", f"Alarm will trigger {minutes_before} minutes before the scheduled time.")

    def show_popup(self, title, message):
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text=message))
        close_button = Button(text="Close", size_hint=(None, None), width=200, height=50)
        content.add_widget(close_button)
        popup = Popup(title=title, content=content, size_hint=(None, None), size=(400, 200))
        close_button.bind(on_press=popup.dismiss)
        popup.open()


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(ScheduleScreen(name='schedule'))
        return sm


if __name__ == '__main__':
    MyApp().run()
