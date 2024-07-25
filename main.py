import checkin
import pygui
import pandas
import dearpygui.dearpygui as dpg


class Processor:

    def __init__(self):
        self.chk = checkin.CheckIn()
        self.gui = pygui.InatorGUI()
        self.__main__()

    def __main__(self):
        print("Running")
        #print(self.chk.params.items())
        #self.gui.main()
        #print(self.gui.params.items())

proc = Processor()
#proc.__main__()

print(proc.gui.chk.params.items())
