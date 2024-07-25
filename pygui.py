import dearpygui.dearpygui as dpg
import checkin

class InatorGUI: 

    def __init__(self):
        self.chk = checkin.CheckIn()
        self.main()
        """self.vars = [sleep_time, wakeup_time, if_sleepy, bfast_time, bfast,
                     if_bloated, if_headache, headache_intensity, coffee, 
                    coffee_intensity, if_palpitation, comments]
"""
    def change_text(self, sender, app_data):
        dpg.set_value("text item", f"Mouse Button ID: {app_data}")

    def visible_call(self, sendeSr, app_data):
        #print("I'm visible")
        return

    # The callback argument in add_button takes the name of a function which will execute everytime you press that button.
    # “user_data” is the input you want to give to the button everytime its pressed.
    def on_submit_button_press(self, sender, app_data, user_data):
        print("Callback")
        var_list = [dpg.get_value(i) for i in user_data]
        #print(var_list)
        for i, key in enumerate(self.chk.params):
            self.chk.params[key] = var_list[i]

        #print(self.chk.params.items())
       
        return [dpg.get_value(i) for i in user_data]
    
    def main(self):

        dpg.create_context()
        with dpg.window(label = "Checkin", height= 600, width = 550, no_collapse=True, no_resize=True) as window1:
            with dpg.group(horizontal=True):
                dpg.add_text("Time Slept")
                sleep_time = dpg.add_input_text( no_spaces= True,label= "",  tag = "Time Field 1", tracked = True)
                day_half = dpg.add_combo(["AM", "PM"], default_value= "AM", width= 40)
            
            with dpg.group(horizontal=True):
                dpg.add_text("Time Woken Up")
                wakeup_time = dpg.add_input_text(no_spaces= True,  tag = "Time Field 2", tracked = True)
                day_half = dpg.add_combo(["AM", "PM"], default_value= "AM", width= 40)

            with dpg.group(horizontal=True):
                dpg.add_text("Still Sleepy?")
                if_sleepy = dpg.add_input_text(no_spaces= True, tag = "Bool Field 1", tracked = True)

            with dpg.group(horizontal=True):
                dpg.add_text("Breakfast Time")
                bfast_time = dpg.add_input_text(no_spaces= True, tag = "Time Field 3", tracked = True)
                day_half = dpg.add_combo(["AM", "PM"], default_value= "AM", width= 40)
            
            with dpg.group(horizontal=True):
                dpg.add_text("Breakfast Items")
                bfast = dpg.add_input_text(no_spaces= False, hint = "eg. Cereal, Vegetables, Maggi", tracked = True)

            with dpg.group(horizontal=True):
                dpg.add_text("Bloated?")
                if_bloated = dpg.add_input_text(no_spaces= True, label = "      ", tag = "Bool Field 2" , tracked = True)

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
                if_palpitation = dpg.add_input_text(no_spaces= True, tracked = True)

            with dpg.group(horizontal=True):
                dpg.add_text("Additional Comments")
                comments = dpg.add_input_text(hint = " ", multiline = True, tracked = True)

            dpg.add_button(label = "Save", tag = "Print Button",  user_data= [sleep_time, wakeup_time, if_sleepy, bfast_time, bfast,
                                                                                if_bloated, if_headache, headache_intensity, coffee, 
                                                                                coffee_intensity, if_palpitation, comments], 
                                                                                callback= self.on_submit_button_press)
            w = dpg.get_item_width(window1)
            h = dpg.get_item_height(window1)
            
            
        

        # so either i use callback = func() within the element initialization or use a registry and bind it explicitly
        dpg.create_viewport(title= f'CheckinInator', width= w, height= h, resizable = False, clear_color= (0,0,0))
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()

        return

def __main__():
    return
    #gui = InatorGUI()
if __name__ == "__main__":
    __main__()
#gui.main()
#print(gui.chk.params.items())
