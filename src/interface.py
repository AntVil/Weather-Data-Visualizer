import cartopy
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import sys
import tkinter as Tk


class weather_data_interface:
    def __init__(self):
        self.root = Tk.Tk()
        self.root.wm_title("Weather Data")
        
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
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.root)
        self.toolbar.update()
        

        self.canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

        self.canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

        #Button for testing if the interface works
        self.button = Tk.Button(master=self.root, text='Quit', command=sys.exit)
        self.button.pack(side=Tk.BOTTOM)
        Tk.mainloop()

weather_data_interface()