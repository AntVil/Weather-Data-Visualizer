# this file contains all components needed to plot data on a map
import cartopy
from matplotlib import pyplot as plt
from matplotlib import tri
from dwd import get_dwd_DataFrames
import numpy as np


GERMANY_LOACTIONS = {
    "germany": (5, 16, 56, 46),

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
