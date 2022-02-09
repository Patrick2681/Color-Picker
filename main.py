from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.properties import NumericProperty
import pyperclip

Config.set('graphics', 'width', '350')
Config.set('graphics', 'height', '300')
Config.set('graphics', 'resizable', False)


class CustomColorPicker(BoxLayout):
    code = [0,0,0]
    red, green, blue = NumericProperty(0),NumericProperty(0),NumericProperty(0)
    
    def slider_it(self, *args):
        color, value = args[0], args[2]
        if color == 'red': self.code[0] = int(value)
        if color == 'green': self.code[1] = int(value)
        if color == 'blue': self.code[2] = int(value)
        self.update()   
    
    def update(self):
        self.ids.code_input.text = f"{self.code[0]},{self.code[1]},{self.code[2]}"
        self.red, self.green, self.blue = self.code[0], self.code[1], self.code[2]

    def copy(self, *args):
        rgb_code = f"{self.code[0]},{self.code[1]},{self.code[2]}"
        pyperclip.copy(rgb_code)

class MainApp(App):
    def build(self):
        return CustomColorPicker()


if __name__ == "__main__":
    MainApp().run()
