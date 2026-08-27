#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
# PROJECT   : RegCEl - Registro para el Consumo Eléctrico                                              #
# VERSION   : 1.2                                                                                                      #
# AUTHOR    : Yunior Barceló Chávez             barceloch@gmail.com                                                                         #
# DATE      : 9/01/2021                                                                                               #
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
"""
This file contains different customized widgets

Availabe classes:
-----------------
    - HoverOneLineListItem
    - LabelForList
    - LabelForListStudent
    - AdminInfoLabel
    - AdminInfoEditField
    - CustomRecycleView

"""

from kivymd.uix.list import OneLineListItem
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.bubble import Bubble, BubbleButton
from hoverable import HoverBehavior
from kivy.uix.floatlayout import FloatLayout

from kivy.app import App


class LabelForList(Label):
    """
    This class creates universal label to be used in list items across this application
    """

    pass

class TotalsInfoLabel(BoxLayout):
    """
    Customized `Label` to show personal/credential informations of the admin
    """

    pass

class PanelInfoLabel(BoxLayout):
    """
    Customized `Label` to show personal/credential informations of the admin
    """

    pass


class CustomBubbleButton(BubbleButton):
    
    def add_text(self):
        app= App.get_running_app()
        index=app.root.ids.registerScreen.ids.input_field.cursor[0]-1
        
        if self.text!="<-":
            app.root.ids.registerScreen.ids.input_field.text=app.root.ids.registerScreen.ids.input_field.text[:index+1]+self.text + app.root.ids.registerScreen.ids.input_field.text[index+1:]
            app.root.ids.registerScreen.ids.input_field.cursor=(index+2,0)
        else:
            app.root.ids.registerScreen.ids.input_field.text=app.root.ids.registerScreen.ids.input_field.text[:index] + app.root.ids.registerScreen.ids.input_field.text[index+1:] if index != -1 and app.root.ids.registerScreen.ids.input_field.cursor != (0,0) else app.root.ids.registerScreen.ids.input_field.text
            app.root.ids.registerScreen.ids.input_field.cursor=(index,0)
            
    pass


class NumericKeyboard(Bubble):
    
    def on_touch_up(self, touch):
        app= App.get_running_app()
        if  not self.collide_point(*touch.pos) and not self.parent.collide_point(*touch.pos):
            self.parent.remove_widget(self.parent.bubb)
            app.root.ids.registerScreen.ids.input_field.focus=False
            delattr(app.root.ids.registerScreen.ids.input_field.parent, 'bubb')     
                   
    def __init__(self, **kwargs):
        super(NumericKeyboard, self).__init__(**kwargs)
        self.create_bubble_button()

    def create_bubble_button(self):
        numeric_keypad = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0', '', '<-']
        for x in numeric_keypad:
            if x == '':
                bubb_btn = CustomBubbleButton(disabled=True, text=str(x),font_name='zekton__.ttf', bold=True, font_size="20sp")
            else:    
                bubb_btn = CustomBubbleButton(text=str(x),font_name='zekton__.ttf', bold=True, font_size="20sp")
            self.numeric_keyboard_layout.add_widget(bubb_btn)


class ShowInputBubble(FloatLayout):    
    def show_bubble(self, *l):
        if not hasattr(self, 'bubb'):
            self.bubb = NumericKeyboard()
            self.bubb.arrow_pos = "top_mid"
            self.add_widget(self.bubb)