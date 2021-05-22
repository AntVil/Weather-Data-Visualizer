import cartopy
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import sys
import tkinter as Tk
from tkcalendar import Calendar,DateEntry

class weather_data_interface:
    def __init__(self):
        self.root = Tk.Tk()
        self.root.wm_title("Wetterdaten Visualizer")
        self.root.iconbitmap("./src/images/logo/logo.ico")
        
        #Cartopy TKinter integration
        
        self.fig, self.ax = plt.subplots(figsize=(10, 6))
        
        self.ax.axis('off')
        self.ax = plt.axes(projection=ccrs.PlateCarree())
        

        self.ax.plot(10, 50, 'bo', markersize=7, transform=ccrs.Geodetic())
        self.ax.text(10, 51, 'test', transform=ccrs.Geodetic())

        self.ax.add_feature(cartopy.feature.LAND)
        self.ax.add_feature(cartopy.feature.OCEAN)
        self.ax.add_feature(cartopy.feature.COASTLINE)
        self.ax.add_feature(cartopy.feature.BORDERS, linestyle=':')
        self.ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
        self.ax.add_feature(cartopy.feature.RIVERS)

        self.ax.set_extent([5, 16, 57, 45])


        #Drawing canvas and toolbar for navigation

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        
        self.toolbarFrame = Tk.Frame(master=self.root)
        self.toolbarFrame.grid(row=1,column=3)
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.toolbarFrame)
        self.toolbar.update()


        #calendar inputs
        self.label_cal_from = Tk.Label(self.root, text="Startdate")
        self.label_cal_till = Tk.Label(self.root, text="Enddate")
        self.cal_from = DateEntry(self.root, width=30, year=2021)
        self.cal_till = DateEntry(self.root, width=30, year=2021)

        self.label_cal_from.grid(column=0, row=1)
        self.label_cal_till.grid(column=0, row=3)
        self.cal_from.grid(column=0, row=2, padx=10, pady=5)
        self.cal_till.grid(column=0, row=4, padx=10, pady=5)
        

         #Location selection
        self.label_location = Tk.Label(self.root, text="Location")
        self.location_list = ["Germany", "Baden-Württemberg","Bayern","Berlin","Brandenburg","Bremen","Hamburg","Hessen","Mecklenburg-Vorpommern","Niedersachsen","Nordrhein-Westfalen","Rheinland-Pfalz","Saarland","Sachsen","Sachsen-Anhalt","Schleswig-Holstein","Thüringen"]
        self.selected_location = Tk.StringVar(self.root) #init location var
        self.selected_location.set(self.location_list[0]) #setting default choice
        self.location = Tk.OptionMenu(self.root, self.selected_location,*self.location_list)
       
        self.label_location.grid(column=0, row=5)
        self.location.config(width=27, background="white", borderwidth=1 )
        self.location.grid(column=0, row=6, padx=10, pady=5)


        #Plotting-type Selection
        self.label_ptype = Tk.Label(self.root, text="select Plotting-Type:")
        self.ptype_var = Tk.IntVar()
        self.ptype_temp = Tk.Radiobutton(self.root, text="Temperature", variable=self.ptype_var, value="1")
        self.ptype_hum = Tk.Radiobutton(self.root, text="Humidity", variable=self.ptype_var, value="2")

        self.ptype_temp.grid(column=0, row=7, padx=5, pady=10)
        self.ptype_hum.grid(column=1, row=7, padx=5, pady=10)

        self.canvas.get_tk_widget().grid(column=3, row=0)
        
        self.canvas._tkcanvas.grid(column=3, row=0)

        
       
        #Button for testing if the interface works
        self.button = Tk.Button(master=self.root, text='Quit', command=sys.exit)
        self.button.grid(column=3, row=2)
        Tk.mainloop()

weather_data_interface()