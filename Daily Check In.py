import checkin
import pygui
import pandas as pd
import dearpygui.dearpygui as dpg
from datetime import datetime as dt
import sys
import traceback

class Processor:

    def __init__(self):
        
        self.chk = checkin.CheckIn()
        self.gui = pygui.InatorGUI()
        self.data_dict = {}
        
        self.func_main()

    def func_main(self):
        
        try:
            self.data_dict = self.gui.append_time_period() # returns gui.chk.params
            
            self.data_dict["Time Slept"] = dt.strptime(self.data_dict["Time Slept"], r"%I:%M %p").time()
            self.data_dict["Wake up Time"] = dt.strptime(self.data_dict["Wake up Time"], r"%I:%M %p").time()
            self.data_dict["Breakfast Time"] = dt.strptime(self.data_dict["Breakfast Time"], r"%I:%M %p").time()
            
            
           
            self.data_dict["Still Sleepy?"] = self.chk.input_str_to_bool(self.data_dict["Still Sleepy?"])
            
                
            
            self.data_dict["Bloated?"] =  self.chk.input_str_to_bool(self.data_dict["Bloated?"])

            
            self.data_dict["Headache"] =  self.chk.input_str_to_bool(self.data_dict["Headache"])
            if self.data_dict["Headache"] == False:
                self.data_dict["Headache Intensity"] = 0.0
                
            
            self.data_dict["Had Coffee"] =  self.chk.input_str_to_bool(self.data_dict["Had Coffee"])
            
            if self.data_dict["Had Coffee"] == False:
                self.data_dict["Strength of Coffee"] = 0.0

            
            self.data_dict["Palpitation?"] =  self.chk.input_str_to_bool(self.data_dict["Palpitation?"])

            print(self.data_dict)

        except Exception as e:
            print(e)
            pass
        

    def append_dict(self, data):

        keys = list(data.keys())
        keys.insert(0, "Date")

        return {k: data.get(k, dt.now().date()) for k in keys}

def __main__():
    #print("running")
    proc = Processor()
    #print(proc.data_dict)
    #updated_dict = proc.append_dict(proc.data_dict)
    #print(updated_dict)
    #df = pd.DataFrame(columns= proc.data_dict.keys())
    df = pd.DataFrame([proc.data_dict])
    
    #print(df)
    #df.to_csv(r"D://programming projects//.py projects\DailyCheckIn\Daily Check In Dataset.csv", index = False, date_format = r"%B %d, %Y %I:%M %p", mode = "w")
    dataset = pd.read_csv(r"D://programming projects//.py projects\DailyCheckIn//Daily Check In Dataset.csv")
    
    
     # Convert dates to a consistent format for comparison
    proc_date = pd.to_datetime(proc.data_dict["Date"]).date()
    last_dataset_date = pd.to_datetime(dataset.iloc[-1,0]).date()

    if proc_date == last_dataset_date:
        #raise ValueError("You have already recorded today's data. In case you believe this error was thrown" +
                         #f" due to an error, delete the entry for {dt.now().date().strftime(r"%d-%m-%Y")} manually from the datasheet.")
        
        sys.exit("You have already recorded today's data. In case you believe this message was thrown" +
                         f" due to an error, delete the entry for {dt.now().date().strftime(r"%d-%m-%Y")} manually from the datasheet located at: "
                         + "D:\programming projects\.py projects\DailyCheckIn")

    
    
    df.to_csv(r"D://programming projects//.py projects\DailyCheckIn\Daily Check In Dataset.csv", index = False, header= None,  date_format = r"%B %d, %Y %I:%M %p", mode = "a")
    
    
    """with pd.ExcelWriter('Daily Check In Dataset.xlsx',
                    mode='a', if_sheet_exists= "overlay") as writer:  
        df.to_excel(writer, sheet_name = "Sheet 1")
"""
    #record.to_csv("Daily Check In Dataset.csv")
    return

if __name__ == "__main__":
    with open(r"D://programming projects//.py projects//DailyCheckIn//log.txt", "r+") as log:
        try:
            __main__()
            #This line opens a log file
            input("Close?")
            # some code
            # Below line will print any print to log file as well.
            print("Creating DB Connection", file = log)
        except Exception as e:
            traceback.print_exc(file=log)
            raise e
            pass
    sys.exit()



