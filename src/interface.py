import cartopy
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure

import sys
import tkinter as Tk


class weather_data_interface:
    def __init__(self):
        self.root = Tk.Tk()
        self.root.wm_title("Weather Data")
        
        #Cartopy TKinter integration
        self.fig = Figure(figsize=(10,6), dpi=100)
        ax = self.fig.add_axes([0.01, 0.01, 0.98, 0.98],projection = cartopy.crs.PlateCarree())
        ax.add_feature(cartopy.feature.LAND)
        ax.add_feature(cartopy.feature.OCEAN)
        ax.add_feature(cartopy.feature.COASTLINE)
        ax.add_feature(cartopy.feature.BORDERS, linestyle=':')
        ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
        ax.add_feature(cartopy.feature.RIVERS)

        ax.set_extent([5, 16, 57, 45])

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