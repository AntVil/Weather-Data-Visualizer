# this file contains all components needed to plot data on a map
import cartopy
from matplotlib import pyplot as plt
from matplotlib import tri
from dwd import get_dwd_DataFrames
import numpy as np


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


if __name__ == "__main__":
    # plotting map of germany
    ax = plt.axes(projection = cartopy.crs.PlateCarree())
    ax.add_feature(cartopy.feature.LAND)
    ax.add_feature(cartopy.feature.OCEAN)
    ax.add_feature(cartopy.feature.COASTLINE)
    ax.add_feature(cartopy.feature.BORDERS, linestyle=':')
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    ax.add_feature(cartopy.feature.RIVERS)
    ax.set_extent(GERMANY_LOACTIONS["germany"])

    # collecting data from dwd
    x = []
    y = []
    z = []
    for df in get_dwd_DataFrames():
        lat = float(df.LON[0])
        lon = float(df.LAT[0])
        temperature = float(df.TEMPERATURE[0])
        if temperature > -50 and temperature < 100:
            x.append(lat)
            y.append(lon)
            z.append(temperature)

    # creating grid
    xi = np.arange(5, 16, 0.1)
    yi = np.arange(46, 56, 0.1)

    # interpolating vaues on grid
    interpolator = tri.LinearTriInterpolator(tri.Triangulation(x, y), z)
    zi = interpolator(*np.meshgrid(xi, yi))

    # plotting
    ax.contourf(xi, yi, zi, levels=14)
    plt.show()
