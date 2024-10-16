from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# Define the KV layout as a string
kv = '''
WindowManager:
    MainWindow:
    SecondWindow:

<MainWindow>:
    name: "main"

    GridLayout:
        cols:1

        GridLayout:
            cols: 2

            Label:
                text: "Password: "

            TextInput:
                id: passw
                multiline: False

        Button:
            text: "Submit"
            on_release:
                app.root.current = "second" if passw.text == "tim" else "main"
                root.manager.transition.direction = "left"


<SecondWindow>:
    name: "second"

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


class WindowManager(ScreenManager):
    pass
# Define the main app
class MyMainApp(App):
    def build(self):
        return Builder.load_string(kv)  # Load the KV layout from the string

if __name__ == "__main__":
    MyMainApp().run()
