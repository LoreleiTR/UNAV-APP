    def on_enter(self):
            app = App.get_running_app()
            user = app.current_user
            if user:
                user_data = app.users[user]
                self.schedule_file = user_data.get("schedule")
                self.schedule = self.load_schedule()
                self.display_schedule()

        def load_schedule(self):
            if os.path.exists(self.schedule_file):
                with open(self.schedule_file, 'r') as f:
                    return f.readlines()
            return []

        def display_schedule(self):
            schedule_label = self.ids.schedule_label
            if self.schedule:
                schedule_label.text = "\n".join(self.schedule)
            else:
                schedule_label.text = "No schedule available."

        def show_alarm_popup(self, message):
            popup = Popup(title='Alarm', content=Label(text=message), size_hint=(0.8, 0.4))
            popup.open()

        def set_alarm(self, class_time):
            # Implement alarm logic here
            self.show_alarm_popup(f"Time for class: {class_time}")