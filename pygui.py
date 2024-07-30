import dearpygui.dearpygui as dpg
import checkin
import re
from datetime import datetime as dt
import sys

class InatorGUI: 

    def __init__(self):

        self.chk = checkin.CheckIn()
        
        #print(self.chk.params)
        self.time_period = self.chk.time_period

        self.main_gui()


    # The callback argument in add_button takes the name of a function which will execute everytime you press that button.
    # “user_data” is the input you want to give to the button everytime its pressed.

    def on_select_callback(self, sender, app_data, user_data):
    
        if sender == "Day Half1":
            

            if len(self.time_period) >= 1:
                self.time_period[0] = dpg.get_value("Day Half1")
            else:
                self.time_period.append(dpg.get_value("Day Half1"))

        elif sender == "Day Half2":
           
            if len(self.time_period) >= 2:
                #print(len(self.time_period))
                self.time_period[1] = dpg.get_value("Day Half2")
            else:
                self.time_period.append(dpg.get_value("Day Half2"))
                #print("works1")
                
        elif sender == "Day Half3":
    
            if len(self.time_period) >= 3:
                #print(len(self.time_period))

                self.time_period[2] = dpg.get_value("Day Half3")
            else:
                self.time_period.append(dpg.get_value("Day Half3"))

    def on_submit_button_press(self, sender, app_data, user_data):
        
        var_list = [dpg.get_value(i) for i in user_data]
        var_list.insert(0, dt.strftime(dt.now().date(), r"%d-%m-%Y"))
        #print(var_list)
        #print(len(var_list))
        #print(len(self.chk.params))
        
        for i, key in enumerate(self.chk.params):
            if var_list[i] != '':
                #print(f"This is var_list for {i}: " + str(var_list[i]))
                #print("This is self.chk.params[key]: " + str(self.chk.params[key]))
                
                self.chk.params[key] = var_list[i]
                #print(f"This is updated self.chk.params for {key}: " + str(self.chk.params[key]))
        
        dpg.configure_item("Window1", show=False)

        #self.proc = processor.Processor(self.chk.params)
        
        #self.proc.__init__(self.chk.params)
        
    def main_gui(self):

        dpg.create_context()

        with dpg.window(tag = "Window1", label = "Checkin", height= 600, width = 550, no_collapse=True, no_resize=True, no_move= True, 
                        no_title_bar= True) as window1:
            
            current_date = dt.now().date()
            #TO IMPROVE: for every item in dict, check its type and call dpg input elements dynamically based on number of elements in dict
            with dpg.group(horizontal=True):
                dpg.add_text("Time Slept")
                sleep_time = dpg.add_input_text(no_spaces= True, label= "",  tag = "Time Field 1", tracked = True)
                day_half1 = dpg.add_combo(["AM", "PM"], tag = "Day Half1", default_value= "AM", width = 40, callback= self.on_select_callback)
                

            with dpg.group(horizontal=True):
                dpg.add_text("Time Woken Up")
                wakeup_time = dpg.add_input_text(no_spaces= True,  tag = "Time Field 2", tracked = True)
                day_half2 = dpg.add_combo(["AM", "PM"], tag = "Day Half2", default_value= "AM", width = 40, callback= self.on_select_callback)
                
                

            with dpg.group(horizontal=True):
                dpg.add_text("Still Sleepy?")
                if_sleepy = dpg.add_input_text(no_spaces= True, tag = "Bool Field 1", tracked = True)

            with dpg.group(horizontal=True):
                dpg.add_text("Breakfast Time")
                bfast_time = dpg.add_input_text(no_spaces= True, tag = "Time Field 3", tracked = True)
                day_half3 = dpg.add_combo(["AM", "PM"], tag = "Day Half3", default_value= "AM", width= 40, callback= self.on_select_callback)
                
            
            with dpg.group(horizontal=True):
                dpg.add_text("Breakfast Items")
                bfast = dpg.add_input_text(no_spaces= False, hint = "eg. Cereal, Vegetables, Maggi", tracked = True)

            with dpg.group(horizontal=True):
                dpg.add_text("Bloated?")
                if_bloated = dpg.add_input_text(no_spaces= True, tag = "Bool Field 2" , tracked = True)

            with dpg.group(horizontal=True):
                dpg.add_text("Headache?")
                if_headache = dpg.add_input_text(no_spaces= True, tracked = True)

            with dpg.group(horizontal=True):
                dpg.add_text("Headache Intensity")
                headache_intensity = dpg.add_input_int(tracked = True)

            with dpg.group(horizontal=True):
                dpg.add_text("Coffee?")
                coffee = dpg.add_input_text(no_spaces= True, tracked = True)

            with dpg.group(horizontal=True):
                dpg.add_text("Coffee Strength")
                coffee_intensity = dpg.add_input_int( tracked = True)

            with dpg.group(horizontal=True):
                dpg.add_text("Palpitations?")
                if_palpitation = dpg.add_input_text(no_spaces = True, tracked = True)

            with dpg.group(horizontal=True):
                dpg.add_text("Additional Comments")
                comments = dpg.add_input_text(hint = " ", multiline = True, tracked = True)

            dpg.add_button(label = "Save", tag = "Print Button",  user_data= [ sleep_time, wakeup_time, if_sleepy, bfast_time, bfast,
                                                                                if_bloated, if_headache, headache_intensity, coffee, 
                                                                                coffee_intensity, if_palpitation, comments], 
                                                                                callback= self.on_submit_button_press)
       

            w = dpg.get_item_width(window1)
            h = dpg.get_item_height(window1)


        # so either i use callback = func() within the element initialization or use a registry and bind it explicitly
        dpg.create_viewport(title= f'CheckinInator', width= w, height= h, resizable = False, clear_color= (0,0,0))
        dpg.set_viewport_resizable(value = False)
        dpg.set_viewport_always_top(value= True)
        dpg.set_primary_window("Window1", True)
        #dpg.set_viewport_small_icon(icon: str) .ico file
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()

        """while dpg.is_dearpygui_running():
            dpg.render_dearpygui_frame()  
"""
        
       
    
    
    def append_time_period(self):
        #print(self.chk.params["Time Slept"])
        self.chk.params["Time Slept"] = self.chk.params["Time Slept"]+ " "+ self.time_period[0]
        self.chk.params["Wake up Time"] = self.chk.params["Wake up Time"]+ " " +self.time_period[1]
        self.chk.params["Breakfast Time"] = self.chk.params["Breakfast Time"]+ " " + self.time_period[2]
        #print(self.chk.params["Time Slept"])
        return self.chk.params
    

def __main__():
    return
    gui = InatorGUI()
    

if __name__ == "__main__":
    __main__()


