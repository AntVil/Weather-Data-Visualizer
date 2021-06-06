# this file contains all components needed to plot data on a map
import cartopy
from matplotlib import pyplot as plt
from matplotlib import tri
from dwd import get_dwd_DataFrames
from shapes import get_geometry
import numpy as np
import cartopy.crs as ccrs
from datetime import datetime as dt, timezone
import math


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
LOWER_BOUND = {
    "Temperature": -50,
    "Humidity": 0
}
UPPER_BOUND = {
    "Temperature": 100,
    "Humidity": 100
}


def plot_map(save_to, data_type, plot_stations, time, location):
    """
    this function gets data from get_dwd_DataFrames() and generates the plot image for specified user input

    data_type requires string "Temperature" or "Humidity"
    plot_stations requires boolean value (plot weather Station locations: True/False)
    time requires datetime (dt(...))
    location requires string from GERMANY_LOCATIONS
    """

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
        # calc index in DataFrame (using timestamp)
        index = math.floor((time.timestamp() - df.TIME[0].timestamp()) // 3600)
        if index in df.index:
            lon = float(df.iloc[index].LON)
            lat = float(df.iloc[index].LAT)
            # get requested value (either "temperature" or "humidity")
            value = float(df.iloc[index][data_type.upper()])
            # check respective bounds
            if LOWER_BOUND[data_type] <= value < UPPER_BOUND[data_type]:
                x.append(lon)
                y.append(lat)
                z.append(value)


    # creating grid
    xi = np.arange(GERMANY_LOACTIONS[location][0], GERMANY_LOACTIONS[location][1] + 1, 0.1)
    yi = np.arange(GERMANY_LOACTIONS[location][3], GERMANY_LOACTIONS[location][2] + 1, 0.1)

    # interpolating values on grid
    interpolator = tri.LinearTriInterpolator(tri.Triangulation(x, y), z)
    zi = interpolator(*np.meshgrid(xi, yi))

    # plotting

    hum_min = 30
    hum_max = 100
    temp_min = -20
    temp_max = 40

    if data_type =="Humidity":
        levels = np.arange(hum_min, hum_max+1, 5)
        contour = ax.contourf(xi, yi, zi, levels=levels, vmin=hum_min, vmax=hum_max)
        label = f"{data_type} in %"
    if data_type =="Temperature":
        levels = np.arange(temp_min, temp_max, 2)
        contour = ax.contourf(xi, yi, zi, levels=levels, vmin=temp_min, vmax=temp_max)
        label = f"{data_type} in °C"

    plt.colorbar(contour, ax=ax, label=label)

    font = {'family':'sans-serif','size':10}
    plt.title(time.strftime(f"{location}, %d.%m.%Y"), loc = 'left', fontdict=font)

    if plot_stations:
        ax.scatter(x,y, color="black", s=3, alpha=.6)

    
    if save_to is None:
        plt.show()
    else:
        plt.savefig(save_to, bbox_inches='tight', pad_inches=0, dpi=900)
    plt.close()


if __name__ == "__main__":
    plot_map(
        save_to = None,
        data_type = "Humidity",
        plot_stations = False,
        time = dt(2011, 7, 7, 1, tzinfo=timezone.utc),
        location = "Germany"
    )
