"""
scope:
DailyCheckIn 2024
With GUI
Ask a series of checks to the user, eg. "Breakfast time", "Breakfast", "Bloated?", "Wake up time?"
ask every day, if not asked for several days ask at once for all
store data in excel sheet
visualize data periodically, like this week or today
new row every day
"""
#started 11:30 am on 20/07/24

from datetime import datetime as dt
import os
import openpyxl

import re
import dearpygui.dearpygui as dpg


class CheckIn:

    def __init__(self):
        
        self.sleep_time : dt = dt.now()
        self.wakeup_time : dt = dt.now()
        self.if_sleepy : bool = True
        self.bfast_time : dt = dt.now()
        self.bfast : list = []
        self.if_bloated : bool =  True
        self.if_headache: bool =  True
        self.headache_intensity: float = 0.0
        self.coffee : bool = True
        self.coffee_strength: float = 0.0
        self.if_palpitation: bool =  True
        self.comments : str =  ""


        self.params = { "Time Slept" : self.sleep_time, 
                        "Still Sleepy?" : self.if_sleepy, 
                        "Wake up Time" : self.wakeup_time, 
                        "Breakfast Time" : self.bfast_time, 
                        "What did I have for breakfast?" : self.bfast, 
                        "Bloated?" : self.if_bloated, 
                        "Headache" : self.if_headache, 
                        "Intensity of Headache?" : self.headache_intensity, 
                        "Had Coffee" : self.coffee, 
                        "Strength of Coffee" : self.coffee_strength, 
                        "Palpitation?" : self.if_palpitation, 
                        "Any additional comments?" : self.comments
                       }
        
        #self.show_gui()

    def input_str_to_bool(self, string : str):

        if re.search(r"[+Y][+E]*[S|ah|t]", string, re.IGNORECASE):
            return True
        elif re.search(r"[+N][+O]*[p|e]", string, re.IGNORECASE):
            return False
        raise ValueError("Value must be Positive or Negative. Try yes or no.")
    #completed 1:16 pm

    def input_time(self, string : str):

        time = input(string)
        x = dt.strptime(time, r"%I:%M %p")
        return x

    def get_formatted_current_datetime(self):

        time = dt.now()
        current_date = dt.now().strftime(r"%B %d, %Y")
        current_time = dt.now().strftime(r"%I:%M %p")
        
        return current_date, current_time

    def format_input_datetime(self, input_dt):

        formatted_time = input_dt.strptime(r"%I:%M %p") #string parse time; str -> time
        return formatted_time
    """
    The main script must always:

    Create the context create_context

    Create the viewport create_viewport

    Setup dearpygui setup_dearpygui

    Show the viewport show_viewport

    Start dearpygui start_dearpygui

    Clean up the context destroy_context
    """

    
        

def __main__():
    chk = CheckIn()
    print(chk.bfast)
    return

if __name__ == "__main__":
    __main__()

