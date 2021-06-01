# Weather-Data-Visualizer

### The data
The data is located on the [dwd server](https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/hourly/air_temperature/historical/), accessing their website we get this view:
<br>![](./images/data.png)<br>
Each file can be downloaded and unzipped:
<br>![](./images/zipfile.png)<br>
The measurements are in a csv-format and contain the date, temperature, relative humidity and other values:
<br>![](./images/measurements.png)<br>
But some values are missing or replaced by `-999`:
<br>![](./images/missing_data.png)<br>
The geography is also in csv-format:
<br>![](./images/geography.png)<br>
The measurements are spatially not always at the same place. Some timeranges don't even have a location. Often the end date of the last timerange is not given.

The file [dwd.py](../src/dwd.py) is responsable for downloading the zipfiles and converting them to a more flexible format.
The results are [pandas DataFrames](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas-dataframe) stored as [parquet-files](https://www.youtube.com/watch?v=VZykcApkz_4).
<br>![](./images/dataframe.png)<br>
The date information is converted to `utc` [datetimes](https://docs.python.org/3/library/datetime.html) and all other values are converted either to int or float to reduce file size.

### Plotting
To create plots of maps [matplotlib](https://matplotlib.org/) and [Cartopy](https://scitools.org.uk/cartopy/docs/latest/matplotlib/intro.html) work together:
<br>![](./images/cartopy_map.png)<br>
The map can be cropped to only display germany:
<br>![](./images/cartopy_germany.png)<br>
By downloading the shapefiles of administrative areas in germany from [GADM](https://gadm.org/download_country_v3.html), more context can be added to the plots:
<br>![](./images/germany_administrative_areas.png)<br>
Since the license of `GADM` doesn't permit further distribution the file [shapes.py](../src/shapes.py) downloads and saves the shapefiles locally.

The plot can be further cropped to specific locations:
<br>![](./images/germany_administrative_areas_folder.png)<br>
Using [dwd.py](../src/dwd.py) we can get the coordinates of the stations and plot them on the map:
<br>![](./images/stations.png)<br>
The subpackage [matplotlib.tri](https://matplotlib.org/stable/gallery/images_contours_and_fields/irregulardatagrid.html) makes it possible to interpolate values between the stations, like temperature:
<br>![](./images/interpolated.png)<br>

The file [plot.py](../src/plot.py) is responsable for 

### Converting to video
Using [imageio](https://imageio.readthedocs.io/en/stable/) and the special plugin `imageio-ffmpeg` images like these:
<br>![](./images/test_images.png)<br>
can be converted to a `mp4` video or `gif` like this (`gif` for easy display):
<br>![](./images/test_video_as_gif.gif)<br>

The file [image_to_video.py](../src/image_to_video.py) makes this conversion.

### The Interface
Using [excalidraw](https://excalidraw.com/) a basic wireframe of the interface can be created:
<br>![](./images/interface_mockup.png)<br>

The logo of this project was created using [gimp](https://www.gimp.org/):
<br>![](./images/gimp_logo.png)<br>

Using the library [Eel](https://github.com/ChrisKnott/Eel) an interface can be build using `HTML/CSS/JS`. This library specializes in creating simple interfaces for offline python applications. ([tutorial](https://medium.com/@utsav_datta/create-html-user-interface-for-python-using-eel-library-bab101cc0f99))
<br>![](./images/eel_gui.png)<br>
Eel helps to structure the project more and in addition to that it doesn't have as many limitations as Tkinter.
