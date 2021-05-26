# Weather-Data-Visualizer

### The data
The data is located on the [dwd server](https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/hourly/air_temperature/historical/), accessing their website we get this view:
![](./images/data.png)
Each file can be downloaded and unzipped:
![](./images/zipfile.png)
The measurements are in a csv-format and contain the date, temperature and relative humidity and other values:
![](./images/measurements.png)
But some values are missing or replaced by `-999`:
![](./images/missing_data.png)
The geography is also in csv-format:
![](./images/geography.png)
The measurements are spatially not always at the same place. Some timeranges don't even have a location. Often the end date of the last timerange is not given.

The file [dwd.py](../src/dwd.py) is responsable for downloading the zipfiles and converting them to a more flexible format.
The results are [pandas DataFrames](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas-dataframe) stored as [parquet-files](https://www.youtube.com/watch?v=VZykcApkz_4).
![](./images/dataframe.png)
The date information is converted to `utc` [datetimes](https://docs.python.org/3/library/datetime.html) and all other values are converted either to int or float to reduce file size.

### Plotting
To create plots of maps [matplotlib](https://matplotlib.org/) and [Cartopy](https://scitools.org.uk/cartopy/docs/latest/matplotlib/intro.html) work together:
![](./images/cartopy_map.png)
The map can be cropped to only display germany:
![](./images/cartopy_germany.png)
or any part of germany:
![image of folder with images here!]()
Using [dwd.py](../src/dwd.py) we can get the coordinates of the stations and plot them on the map:
![](./images/stations.png)
The subpackage [matplotlib.tri](https://matplotlib.org/stable/gallery/images_contours_and_fields/irregulardatagrid.html) makes it possible to interpolate values between the stations:
![](./images/interpolated.png)

The file [plot.py](../src/plot.py) is responsable for 

### Converting to video
Using [cv2](https://pypi.org/project/opencv-python/) images like these:
![](./images/test_images.png)
can be converted to a `mp4` video like this (converted to `gif` for easy display):
![](./images/test_video_as_gif.gif)

The file [image_to_video.py](../src/image_to_video.py) makes this conversion.

### The Interface
Using [excalidraw](https://excalidraw.com/) a basic wireframe of the interface can be created:
![](./images/interface-mockup.png)

Using the library [Eel](https://github.com/ChrisKnott/Eel) an interface can be build using `HTML/CSS/JS`. This library specializes in creating simple interfaces for offline python applications. ([tutorial](https://medium.com/@utsav_datta/create-html-user-interface-for-python-using-eel-library-bab101cc0f99))
![](./images/eel_gui.png)
Eel helps to structure the project more and in addition to that it doesn't have as many limitations as Tkinter.
The logo of this project was created using [gimp](https://www.gimp.org/)
