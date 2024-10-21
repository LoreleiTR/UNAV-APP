import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from datetime import datetime, timedelta

class ClockApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Display for current Philippine time
        self.time_label = Label(text=self.get_philippine_time(), font_size=40)
        self.layout.add_widget(self.time_label)

        # Spinner (Dropdown) to select alarm time
        self.alarm_spinner = Spinner(
            text='Set Alarm',
            values=['06:00 AM', '07:00 AM', '08:00 AM', '12:52 AM', '01:00 PM', '05:00 PM', '08:00 PM', '09:00 PM'],
            size_hint=(None, None),
            size=(200, 50)
        )
        self.alarm_spinner.bind(text=self.set_alarm)
        self.layout.add_widget(self.alarm_spinner)

        # Button to manually check for alarm
        self.check_button = Button(text="Check Alarm", size_hint=(None, None), size=(200, 50))
        self.check_button.bind(on_press=self.check_alarm)
        self.layout.add_widget(self.check_button)

        # Load the ding sound
        self.alarm_sound = SoundLoader.load('ding.wav')

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
        # Play the ding sound when the alarm is triggered
        if self.alarm_sound:
            self.alarm_sound.play()

        # Create popup with Stop and Snooze options
        alarm_popup = Popup(title="Alarm!", size_hint=(None, None), size=(300, 200))
        alarm_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        alarm_message = Label(text="Your alarm is ringing!")
        stop_button = Button(text="Stop Alarm", on_press=self.stop_alarm)
        snooze_button = Button(text="Snooze 1 min", on_press=lambda instance: self.snooze_alarm(alarm_popup))

        alarm_layout.add_widget(alarm_message)
        alarm_layout.add_widget(stop_button)
        alarm_layout.add_widget(snooze_button)

        alarm_popup.content = alarm_layout
        alarm_popup.open()

    def stop_alarm(self, instance):
        if self.alarm_sound:
            self.alarm_sound.stop()  # Stop the sound

    def snooze_alarm(self, popup):
        # Snooze the alarm for 1 minute
        popup.dismiss()  # Close the current alarm popup
        snooze_time = (datetime.now() + timedelta(minutes=1)).strftime("%I:%M %p")
        self.alarm_time = snooze_time  # Set new alarm time 1 minute later
        snooze_popup = Popup(title="Snooze", content=Label(text="Alarm snoozed for 1 minute"), size_hint=(None, None), size=(300, 200))
        snooze_popup.open()

if __name__ == '__main__':
    ClockApp().run()
