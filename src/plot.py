# this file contains all components needed to plot data on a map
import cartopy
from matplotlib import pyplot as plt
from matplotlib import tri
from dwd import get_dwd_DataFrames
from shapes import get_geometry
import numpy as np
import cartopy.crs as ccrs
from datetime import datetime as dt, tzinfo
import pytz

#constants
GERMANY_LOACTIONS = {
    "Germany": (5, 16, 56, 46),
    "Baden-Württemberg": (7, 11, 50, 47),
    "Bayern": (8.5, 14, 51, 47),
    "Berlin": (12.87, 13.9, 52.8, 52.2),
    "Brandenburg": (11, 15.5, 53.8, 51.1),
    "Bremen": (8.4, 9.1, 53.3, 52.88),
    "Hamburg": (9.5, 10.55, 53.85, 53.25),
    "Hessen": (7.66, 10.45, 51.8, 49.3),
    "Mecklenburg-Vorpommern": (10.4, 14.7, 54.85, 52.93),
    "Niedersachsen": (6.5, 11.73, 54, 51.23),
    "Nordrhein-Westfalen": (5.6, 9.65, 52.85, 50.1),
    "Rheinland-Pfalz": (5.93, 8.54, 51.12, 48.82),
    "Saarland": (6.26, 7.47, 49.75, 48.97),
    "Sachsen": (11.74, 15.15, 51.76, 50.08),
    "Sachsen-Anhalt": (10.36, 13.32, 53.11, 50.88),
    "Schleswig-Holstein": (8.07, 11.45, 55.15, 53.26),
    "Thüringen": (9.64, 12.8, 51.72, 50.15),
}


def plot_map(save_to, data_type, plotting_type, time, location):
    """
    this function 

    data_type needs to be set to "temperature" or "humidity"
    plotting_type needs to be set to "interpolation" or "scatter"
    time needs to be single point in time
    location needs to be a string from GERMANY_LOCATIONS
    """
    pass


if __name__ == "__main__":
    # plotting map of germany
    
    location = "Thüringen" #testdata, will be from plot_map argument "location"
    data_type = "temperature"
    plotting_type = "interpolation"
    time = dt(2011,3,1,19,0,0,0,pytz.UTC)

    ax = plt.axes(projection = cartopy.crs.PlateCarree())
    
    ax.set_extent(GERMANY_LOACTIONS[location])

    ax.add_feature(cartopy.feature.LAND)
    ax.add_feature(cartopy.feature.OCEAN)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    ax.add_feature(cartopy.feature.RIVERS)
    ax.add_feature(cartopy.feature.COASTLINE)
    ax.add_geometries(get_geometry(level=1), ccrs.PlateCarree(), edgecolor='black', facecolor='gray', alpha=0.2)
    ax.add_feature(cartopy.feature.BORDERS, linestyle=':')


    
    # collecting data from dwd
    
    x = []
    y = []
    z = []
    for df in get_dwd_DataFrames():

        #gets corresponding data for selected time
    
        if df.LON[df["TIME"] == time].values.size != 0: # checks if Pandas.Series object "values" argument is not empty
            lon = float(df.LON[df["TIME"] == time].values[0]) # assigns value to variable
        if df.LAT[df["TIME"] == time].values.size != 0:
            lat = float(df.LAT[df["TIME"] == time].values[0])
       
        if data_type == "temperature": #checks for data_type ...
            if df.TEMPERATURE[df["TIME"] == time].values.size != 0: # ... and datavalue limits
                temperature = float(df.TEMPERATURE[df["TIME"] == time].values[0])
            if temperature > -50 and temperature < 100:
                x.append(lon)
                y.append(lat)
                z.append(temperature)

        elif data_type == "humidity":
            if df.HUMIDITY[df["TIME"] == time].values.size != 0:
                humidity = float(df.HUMIDITY[df["TIME"] == time].values[0])
            if humidity >= 0 and humidity <= 100:
                print("humidity success")
                x.append(lat)
                y.append(lon)
                z.append(humidity)


    # creating grid
    xi = np.arange(GERMANY_LOACTIONS[location][0], GERMANY_LOACTIONS[location][1], 0.1)
    yi = np.arange(GERMANY_LOACTIONS[location][3], GERMANY_LOACTIONS[location][2], 0.1)

    
    
    # interpolating values on grid
    interpolator = tri.LinearTriInterpolator(tri.Triangulation(x, y), z)
    zi = interpolator(*np.meshgrid(xi, yi))

    # plotting
    ax.contourf(xi, yi, zi, levels=14)
    
    
    plt.show()

    #plt.savefig(f"{location}.png", bbox_inches='tight', pad_inches=0, dpi=900)
    plt.close()
