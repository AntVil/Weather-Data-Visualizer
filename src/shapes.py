# this file contains all components needed to collect, structure and save the data from GADM
import os
import requests
from zipfile import ZipFile
from io import BytesIO
import cartopy.io.shapereader as shpreader
from requests.api import get


# constants
SHAPES_URL = "https://biogeo.ucdavis.edu/data/gadm3.6/shp/gadm36_DEU_shp.zip"
SHAPES_FOLDER = os.path.join(os.path.dirname(__file__), "data", "shapes")
os.makedirs(SHAPES_FOLDER, exist_ok = True)


def download_shapes():
    """
    this function downloads data from GADM
    """

    unpacked = ZipFile(BytesIO(requests.get(SHAPES_URL).content))
    file_names = list(set([file.split(".")[0] for file in unpacked.namelist()]).difference({"license"}))

    # saving license
    with unpacked.open("license.txt", "r") as read_file:
        with open(os.path.join(SHAPES_FOLDER, "license.txt"), "wb") as write_file:
            write_file.write(read_file.read())

    #downloading files
    for file in file_names:
        for extension in [".shp", ".shx", ".dbf"]:
            with unpacked.open(file + extension, "r") as read_file:
                # creating folder structure
                path = os.path.join(SHAPES_FOLDER, file)
                os.makedirs(path, exist_ok = True)
                
                # saving file
                file_name = "shape" + extension
                with open(os.path.join(path, file_name), "wb") as write_file:
                    write_file.write(read_file.read())


def get_geometry(level=1):
    """
    this function returns the administrative-area geometries for germany
    """
    
    try:
        return list(
            shpreader.Reader(
                os.path.join(os.path.dirname(__file__), "data", "shapes", f"gadm36_DEU_{level}", "shape")
            ).geometries()
        )
    except:
        download_shapes()
        return get_geometry(level)


if __name__ == "__main__":
    download_shapes()
