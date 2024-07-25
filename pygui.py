import dearpygui.dearpygui as dpg
import checkin

dpg.create_context()

def change_text(sender, app_data):
    dpg.set_value("text item", f"Mouse Button ID: {app_data}")

def visible_call(sender, app_data):
    #print("I'm visible")
    return

def store_on_button_press(sender, app_data, user_data):
    print("yes")
    print(dpg.get_value(user_data[0]))
    x = dpg.get_value(user_data[0])
    return x
    #print({user_data})
    
with dpg.window(width=1000, height=1000, pos = [0,0]):
    dpg.add_text("Click me with any mouse button", tag="text item")
    b7 = dpg.add_button(label = "Clicky", tag = "submit button")
    dpg.add_text("Close window with arrow to change visible state printing to console", tag="text item 2")
    x = dpg.add_input_float(label = "X")
    dpg.add_button(label="Print", callback= store_on_button_press , user_data=[x])

# The callback argument in add_button takes the name of a function which will execute everytime you press that button.
# “user_data” is the input you want to give to the button everytime its pressed.
    
   
print("This is x: " + str(store_on_button_press))
    
    
with dpg.item_handler_registry(tag="widget handler") as handler:
    dpg.add_item_clicked_handler(callback=change_text)
    dpg.add_item_visible_handler(callback=visible_call)

with dpg.item_handler_registry(tag= "submit button handler") as handler:
    dpg.add_item_clicked_handler(callback = store_on_button_press)


# bind item handler registry to item
dpg.bind_item_handler_registry("submit button", "submit button handler")
dpg.bind_item_handler_registry("text item 2", "widget handler")

dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

chk = checkin.CheckIn()
print(chk.bfast)
