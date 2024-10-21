import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.clock import Clock
from datetime import datetime

class ClockApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Display for current Philippine time
        self.time_label = Label(text=self.get_philippine_time(), font_size=40)
        self.layout.add_widget(self.time_label)

        # Spinner (Dropdown) to select alarm time
        self.alarm_spinner = Spinner(
            text='Set Alarm',
            values=['06:00 AM', '07:00 AM', '08:00 AM', '12:47 AM', '01:00 PM', '05:00 PM', '08:00 PM', '09:00 PM'],
            size_hint=(None, None),
            size=(200, 50)
        )
        self.alarm_spinner.bind(text=self.set_alarm)
        self.layout.add_widget(self.alarm_spinner)

        # Button to manually check for alarm
        self.check_button = Button(text="Check Alarm", size_hint=(None, None), size=(200, 50))
        self.check_button.bind(on_press=self.check_alarm)
        self.layout.add_widget(self.check_button)

        # Scheduled clock update
        Clock.schedule_interval(self.update_time, 1)

        return self.layout

    def get_philippine_time(self):
        # Get current time in the Philippines
        philippine_time = datetime.now().strftime("%I:%M:%S %p")
        return philippine_time

    def update_time(self, *args):
        # Update the clock display
        self.time_label.text = self.get_philippine_time()
        
        # Check if alarm matches the current time
        self.check_alarm(None)

    def set_alarm(self, spinner, text):
        self.alarm_time = text
        popup = Popup(title="Alarm Set", content=Label(text=f"Alarm set for {text}"), size_hint=(None, None), size=(300, 200))
        popup.open()

    def check_alarm(self, instance):
        current_time = datetime.now().strftime("%I:%M %p")
        if hasattr(self, 'alarm_time') and current_time == self.alarm_time:
            self.trigger_alarm()

    def trigger_alarm(self):
        # Display popup or play sound when alarm triggers
        popup = Popup(title="Alarm!", content=Label(text="Your alarm is ringing!"), size_hint=(None, None), size=(300, 200))
        popup.open()

if __name__ == '__main__':
    ClockApp().run()
