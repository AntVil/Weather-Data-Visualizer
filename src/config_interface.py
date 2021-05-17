
#file is to be merged with interface.py in the future

from tkinter import *
from tkcalendar import Calendar,DateEntry


class main_UI:
    def __init__(self):
        self.root = Tk()
        self.root.iconbitmap("./src/images/logo/logo.ico")
        self.root.title("Wetterdaten Visualizer")
        self.root.geometry("500x300")


        #calendar inputs
        self.label_cal_from = Label(self.root, text="Startdate")
        self.label_cal_till = Label(self.root, text="Enddate")
        self.cal_from = DateEntry(self.root, width=30, year=2021)
        self.cal_till = DateEntry(self.root, width=30, year=2021)

        self.label_cal_from.grid(column=0, row=0)
        self.label_cal_till.grid(column=0, row=2)
        self.cal_from.grid(column=0, row=1, padx=10, pady=5)
        self.cal_till.grid(column=0, row=3, padx=10, pady=5)


        #Location selection
        self.label_location = Label(self.root, text="Location")
        self.location_list = ["Germany", "Baden-Württemberg","Bayern","Berlin","Brandenburg","Bremen","Hamburg","Hessen","Mecklenburg-Vorpommern","Niedersachsen","Nordrhein-Westfalen","Rheinland-Pfalz","Saarland","Sachsen","Sachsen-Anhalt","Schleswig-Holstein","Thüringen"]
        self.selected_location = StringVar(self.root) #init location var
        self.selected_location.set(self.location_list[0]) #setting default choice
        self.location = OptionMenu(self.root, self.selected_location,*self.location_list)
       
        self.label_location.grid(column=0, row=4)
        self.location.config(width=27, background="white", borderwidth=1 )
        self.location.grid(column=0, row=5, padx=10, pady=5)


        #Plotting-type Selection
        self.label_ptype = Label(self.root, text="select Plotting-Type:")
        self.ptype_var = IntVar()
        self.ptype_temp = Radiobutton(self.root, text="Temperature", variable=self.ptype_var, value="1")
        self.ptype_hum = Radiobutton(self.root, text="Humidity", variable=self.ptype_var, value="2")

        self.ptype_temp.grid(column=0, row=6, padx=5, pady=10)
        self.ptype_hum.grid(column=1, row=6, padx=5, pady=10)


        self.root.mainloop()

ui = main_UI()