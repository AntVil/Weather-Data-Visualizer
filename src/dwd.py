# this file contains all components needed to collect, format and save the data from dwd
import os
import re
import requests
from zipfile import ZipFile
from io import TextIOWrapper, BytesIO
import csv
import pandas as pd
import numpy as np
import datetime


# constants
DWD_FOLDER = os.path.join(os.path.dirname(__file__), "data", "dwd")
DWD_URL_HISTORICAL = "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/hourly/air_temperature/historical/"
DWD_URL_RECENT = "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/hourly/air_temperature/recent/"


def get_unpacked_zips(*urls):
    """
    this function is a generator which downloads and unzips all .zip files from an url
    """

    for url in urls:
        html = str(requests.get(url).content)
        for zip_link in [f"{url}{link}" for link in re.findall(r'href="(\w*\.zip)"', html)]:
            yield ZipFile(BytesIO(requests.get(zip_link).content))


def download_dwd(*urls):
    """
    this function downloads data from dwd and saves it as an parquet. (default urls are historical & recent)
    """

    if len(urls) == 0:
        urls = [
            DWD_URL_HISTORICAL,
            DWD_URL_RECENT
        ]
    
    for url in urls:
        if not "https://opendata.dwd.de/" in url:
            raise Exception(f"The url '{url}' is not supported, only urls from 'https://opendata.dwd.de/' are supported.")
    
    for unpacked in get_unpacked_zips(*urls):
        data_files = [f for f in unpacked.namelist() if ".txt" in f]
        
        meta_data_file = [f for f in data_files if "Metadaten_Geographie" in f][0]
        main_data_file = [f for f in data_files if "produkt_tu_stunde" in f][0]

        station_id = int(main_data_file.split("_")[-1].split(".")[0])

        # reading main data
        with unpacked.open(main_data_file, "r") as main_data:
            station_df = pd.DataFrame(
                csv.DictReader(TextIOWrapper(main_data, 'utf-8'), delimiter=';')
            ).drop(["STATIONS_ID", "QN_9", "eor"], axis="columns")
            station_df.columns = ["TIME", "TEMPERATURE", "HUMIDITY"]
            station_df.TIME = pd.to_datetime(station_df.TIME, format="%Y%m%d%H", utc=True)

            # adding missing rows
            station_df = pd.merge(
                pd.DataFrame({"TIME": pd.date_range(
                    station_df.TIME.min(),
                    station_df.TIME.max(),
                    freq = "1H",
                    tz = "utc"
                )}),
                station_df,
                how = "outer"
            ).fillna(-999)

            # clean up
            station_df.TEMPERATURE = pd.to_numeric(station_df.TEMPERATURE, downcast="float")
            station_df.HUMIDITY = pd.to_numeric(station_df.HUMIDITY, downcast="integer")
            station_df.sort_values(by="TIME", inplace=True)

        # add coordinates from meta data
        with unpacked.open(meta_data_file, "r") as meta_data:
            meta_df = pd.DataFrame(
                csv.DictReader(TextIOWrapper(meta_data, 'latin-1'), delimiter=';')
            ).drop(["Stations_id", "Stationsname"], axis="columns")
            meta_df.columns = ["ASL", "LAT", "LON", "START", "END"]

            meta_df.iloc[-1].END = datetime.datetime.now().strftime("%Y%m%d")

            meta_df.START = pd.to_datetime(meta_df.START, format="%Y%m%d", utc=True)
            meta_df.END = pd.to_datetime(meta_df.END, format="%Y%m%d", utc=True)

            start = station_df.TIME.min()
            end = station_df.TIME.max() + datetime.timedelta(hours=1)

            lat = np.array([])
            lon = np.array([])
            asl = np.array([])
            for i, entry in meta_df.iterrows():
                a = max((entry.END - start).total_seconds() // 3600 + 24, 0)
                b = max((entry.START - start).total_seconds() // 3600, 0)
                c = max((entry.END - end).total_seconds() // 3600 + 24, 0)
                
                hours = max(int(a - b - c), 0)

                lat = np.append(lat, np.repeat(entry.LAT, hours))
                lon = np.append(lon, np.repeat(entry.LON, hours))
                asl = np.append(asl, np.repeat(entry.ASL, hours))
            
            station_df["LAT"] = lat
            station_df["LON"] = lon
            station_df["ASL"] = asl
        station_df["STATION_ID"] = station_id
        
        # saving
        file_name = f"dwd_station_{str(station_id).zfill(5)}.parquet"
        if file_name in os.listdir(DWD_FOLDER):
            station_df = pd.merge(
                pd.read_parquet(os.path.join(DWD_FOLDER, file_name)),
                station_df,
                how="outer",
            )            
        station_df.to_parquet(os.path.join(DWD_FOLDER, file_name))


if __name__ == "__main__":
    download_dwd()
