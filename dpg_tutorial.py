import dearpygui.dearpygui as dpg 

dpg.create_context()

"""
def on_submit_button_press(sender, app_data, user_data):
    print("Works")
    #x = dpg.get_value("Numerical Field")
    x = dpg.get_value("Numerical Field")
    y = dpg.get_value("Numerical Field 2")
    print(x, y)
    return x
x = 0
with dpg.window(label = "Checkin", height= 600, width = 800):
    dpg.add_input_int(label= "Enter Number", user_data= x, tag = "Numerical Field")
    dpg.add_button(label = "Print", tag = "Print Button", callback= on_submit_button_press)
    dpg.add_input_int(label= "Enter Second Number", user_data= x, tag = "Numerical Field 2")


with dpg.item_handler_registry(tag = "Print Button Handler"):
    dpg.add_item_clicked_handler(callback= on_submit_button_press)

dpg.bind_item_handler_registry("Print Button", "Print Button Handler")
"""

"""def on_submit_button_press(sender, app_data, user_data):
    print("Works")
    #x = dpg.get_value("Numerical Field")
    x = dpg.get_value(firstNum)
    y = dpg.get_value("Numerical Field 2")
    #print(firstNum, secondNum)
    print(x,y)
    #print(user_data)
    return x,y
x = 0
y = 0
with dpg.window(label = "Checkin", height= 600, width = 800):
    firstNum = dpg.add_input_int(label= "Enter Number",  callback= on_submit_button_press, tag = "Numerical Field")
    #dpg.add_button(label = "Print", tag = "Print Button")
    secondNum = dpg.add_input_int(label= "Enter Second Number", callback= on_submit_button_press, tag = "Numerical Field 2")"""

def on_submit_button_press(sender, app_data, user_data):
    #print("Works")
    #x = dpg.get_value("Numerical Field")
    x = dpg.get_value(firstNum)
    y = dpg.get_value("Numerical Field 2")
    #print(firstNum, secondNum)
    #print(x,y)
    print(dpg.get_value(user_data[0]))
    print(dpg.get_value(secondNum))
    return x,y

x = 0
y = 0
#help(dpg.get_item_width)
with dpg.window(label = "Checkin", height= 600, width = 500, no_collapse=True, no_resize=True) as window1:
    firstNum = dpg.add_input_int(label= "Enter Number",  tag = "Numerical Field")
    secondNum = dpg.add_input_int(label= "Enter Second Number", tag = "Numerical Field 2")
    dpg.add_button(label = "Print", tag = "Print Button",  user_data= [firstNum, secondNum], callback= on_submit_button_press)
    w = dpg.get_item_width(window1)
    h = dpg.get_item_height(window1)
#print(dpg.get_value(a))

    
 


# so either i use callback = func() within the element initialization or use a registry and bind it explicitly
dpg.create_viewport(title= f'CheckinInator Day', width= w, height= h, resizable = False, clear_color= (0,0,255))
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()