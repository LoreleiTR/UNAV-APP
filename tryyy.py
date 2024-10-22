import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner
from kivy.clock import Clock
import pygame
import datetime

# Initialize pygame for sound
pygame.mixer.init()

class AlarmApp(App):
    def build(self):
        self.title = "Alarm Scheduler"
        self.layout = BoxLayout(orientation='vertical')
        
        # Schedule label
        self.schedule_label = Label(text="Set Your Schedule (Philippine Time)")
        self.layout.add_widget(self.schedule_label)

        # Create Spinners for Year, Month, Day, Hour, Minute
        self.year_spinner = Spinner(
            text='2024',
            values=[str(year) for year in range(2023, 2030)],
            size_hint=(None, None),
            size=(200, 44)
        )
        self.layout.add_widget(self.year_spinner)

        self.month_spinner = Spinner(
            text='1',
            values=[str(i) for i in range(1, 13)],
            size_hint=(None, None),
            size=(200, 44)
        )
        self.layout.add_widget(self.month_spinner)

        self.day_spinner = Spinner(
            text='1',
            values=[str(i) for i in range(1, 32)],
            size_hint=(None, None),
            size=(200, 44)
        )
        self.layout.add_widget(self.day_spinner)

        self.hour_spinner = Spinner(
            text='12',
            values=[str(i) for i in range(0, 24)],
            size_hint=(None, None),
            size=(200, 44)
        )
        self.layout.add_widget(self.hour_spinner)

        self.minute_spinner = Spinner(
            text='00',
            values=[str(i).zfill(2) for i in range(0, 60)],
            size_hint=(None, None),
            size=(200, 44)
        )
        self.layout.add_widget(self.minute_spinner)

        # Alarm Time dropdown (10 or 5 minutes before)
        self.alarm_label = Label(text="Set Alarm Time Before Schedule")
        self.layout.add_widget(self.alarm_label)
        
        self.alarm_spinner = Spinner(
            text='10 minutes',
            values=('10 minutes', '5 minutes'),
            size_hint=(None, None),
            size=(200, 44)
        )
        self.layout.add_widget(self.alarm_spinner)

        # Set Schedule button
        self.set_button = Button(text="Set Alarm")
        self.set_button.bind(on_press=self.set_alarm)
        self.layout.add_widget(self.set_button)

        return self.layout

    def set_alarm(self, instance):
        # Get the schedule time from the spinners
        year = int(self.year_spinner.text)
        month = int(self.month_spinner.text)
        day = int(self.day_spinner.text)
        hour = int(self.hour_spinner.text)
        minute = int(self.minute_spinner.text)

        # Create the scheduled datetime object
        schedule_time = datetime.datetime(year, month, day, hour, minute)
        alarm_offset = self.alarm_spinner.text

        # Calculate the alarm time (subtracting minutes from schedule)
        if alarm_offset == '10 minutes':
            alarm_time = schedule_time - datetime.timedelta(minutes=10)
        else:
            alarm_time = schedule_time - datetime.timedelta(minutes=5)

        # Schedule the alarm to trigger at the calculated time
        current_time = datetime.datetime.now()
        time_to_alarm = (alarm_time - current_time).total_seconds()

        # Schedule the alarm callback
        if time_to_alarm > 0:
            Clock.schedule_once(self.trigger_alarm, time_to_alarm)
            print(f"Alarm set for {alarm_time} (triggering in {time_to_alarm} seconds)")
        else:
            print("Scheduled time is in the past!")

    def trigger_alarm(self, dt):
        # Play sound using pygame
        pygame.mixer.music.load('alarm/alarm.mp3')
        pygame.mixer.music.play(-1)  # Loop the sound

        # Show the popup notification
        self.show_popup()

    def show_popup(self):
        content = BoxLayout(orientation='vertical')
        label = Label(text="Time's Up! Alarm Triggered!")
        stop_button = Button(text="Stop")
        stop_button.bind(on_press=self.stop_alarm)
        snooze_button = Button(text="Snooze")
        snooze_button.bind(on_press=self.snooze_alarm)

        content.add_widget(label)
        content.add_widget(stop_button)
        content.add_widget(snooze_button)

        self.popup = Popup(title="Alarm Notification", content=content, size_hint=(0.5, 0.5))
        self.popup.open()

    def stop_alarm(self, instance):
        # Stop sound and close popup
        pygame.mixer.music.stop()
        self.popup.dismiss()

    def snooze_alarm(self, instance):
        # Stop sound and snooze (e.g., reset alarm to trigger in 5 minutes again)
        pygame.mixer.music.stop()
        self.popup.dismiss()

        # Reschedule alarm to trigger again in 5 minutes
        Clock.schedule_once(self.trigger_alarm, 5 * 60)  # 5 minutes
        print("Snoozing alarm, will trigger again in 5 minutes.")

if __name__ == '__main__':
    AlarmApp().run()
