# this file contains all components needed to plot data on a map
import cartopy
from matplotlib import pyplot as plt
from dwd import get_dwd_DataFrames

ax = plt.axes(projection = cartopy.crs.PlateCarree())

ax.add_feature(cartopy.feature.LAND)
ax.add_feature(cartopy.feature.OCEAN)
ax.add_feature(cartopy.feature.COASTLINE)
ax.add_feature(cartopy.feature.BORDERS, linestyle=':')
ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
ax.add_feature(cartopy.feature.RIVERS)

ax.set_extent([5, 16, 56, 46])

x = []
y = []
z = []

for df in get_dwd_DataFrames():
    x.append(float(df.LON[0]))
    y.append(float(df.LAT[0]))
    z.append(float(df.TEMPERATURE[0]))

ax.contourf(x, y, z)

plt.show()
