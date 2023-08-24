from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from instructions import txt_instruction, txt_test1, txt_test2, txt_test3, txt_sits
from ruffier import test

from seconds import Seconds
age = 7
name = ""
p1, p2, p3 = 0, 0, 0
def check_int(str_num):
    try:
        return int(str_num)
    except:
        return False


class InstrScr(screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_instruction)
        Lbl1 = Label(text='Введите имя:', halign='right')
        self.in_name = TextInput(multiline=False)
        Lbl2 = Label(text='Введите возраст:', halign='right')
        self.in_age = TextInput(text='7', multiline=False)
        self.btn = Button(text='Начать', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next
        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line1.add_widget(Lbl1)
        line1.add_widget(self.in_name)
        line2.add_widget(Lbl2)
        line2.add_widget(self.in_age)
        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)
        self.add_widget(outer)
    def next(self):
        name = self.in_name
        age = check_int(self.in_age.text)
        if age == False or age < 7:
            age = 7
            self.in_age.text = str(age)
        else:
            self.manager.current = 'pulse1'
class PulseScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False

        instr = Label(text=txt_test1)
        self.Lbl_sec = seconds(15)
        self.Lbl_sec.bind(done=self.sec_finished)
        
        line = BoxLayout(size_hint=(0.8, None), height='30sp')
        Lbl_result = Label(text='Введите результат:',halign='right
        self.in_result = TextInput(text='0', multiline=False)
        self.in_result.set_disabled(True)

        line.add_widget(Lbl_result)
        line.add_widget(self.in_result)
        Self.btn = Button
