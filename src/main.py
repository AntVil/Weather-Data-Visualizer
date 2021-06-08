# this file is the entry point for the project
import eel
import os
import dwd
from plot import plot_map
from image_to_video import image_to_video
import datetime


#constants
INTERFACE_FOLDER = os.path.join(os.path.dirname(__file__), "interface")
INTERFACE_START_FILE = "index.html"
INTERFACE_IMAGE_FOLDER = os.path.join(INTERFACE_FOLDER, "data", "temp", "image")
INTERFACE_VIDEO_FOLDER = os.path.join(INTERFACE_FOLDER, "data", "temp", "video")
TEMP_IMAGE_FOLDER = os.path.join(os.path.dirname(__file__), "data", "temp", "image")
os.makedirs(INTERFACE_IMAGE_FOLDER, exist_ok=True)
os.makedirs(INTERFACE_VIDEO_FOLDER, exist_ok=True)
os.makedirs(TEMP_IMAGE_FOLDER, exist_ok=True)


def clear_dir(dir):
    """
    this function clears the contents of a directory
    """

    for file in os.listdir(dir):
        os.remove(os.path.join(dir, file))


@eel.expose
def data_downloaded():
    """
    returns True if all data from dwd is downloaded
    """

    return dwd.dwd_downloaded()


@eel.expose
def download_data():
    """
    starts the download from dwd
    """

    try:
        dwd.download_dwd(
            dwd.DWD_URL_HISTORICAL,
            dwd.DWD_URL_RECENT
        )
        return True
    except:
        return False


@eel.expose
def render_timepoint(data_type, plot_stations, timestamp, location, ext):
    """
    creates an plot in "interface/data/temp/image" to be shown on the interface
    """

    clear_dir(INTERFACE_IMAGE_FOLDER)
    save_to = os.path.join(INTERFACE_IMAGE_FOLDER, f"result.{ext}")

    plot_map(
        save_to = save_to,
        data_type = data_type,
        plot_stations = plot_stations,
        time = datetime.datetime.fromtimestamp(timestamp, tz=datetime.timezone.utc),
        location = location
    )


@eel.expose
def render_timerange(data_type, plot_stations, timestamp1, timestamp2, location, ext):
    """
    creates mutiple plots and fuses them to a video in "interface/data/temp/video" to be shown on the interface
    """

    clear_dir(TEMP_IMAGE_FOLDER)
    for timestamp in range(timestamp1, timestamp2, 3600):
        plot_map(
            save_to = os.path.join(TEMP_IMAGE_FOLDER, str(timestamp).zfill(12) + ".png"),
            data_type = data_type,
            plot_stations = plot_stations,
            time = datetime.datetime.fromtimestamp(timestamp, tz=datetime.timezone.utc),
            location = location
        )

    clear_dir(INTERFACE_VIDEO_FOLDER)
    image_to_video(
        [os.path.join(TEMP_IMAGE_FOLDER, file) for file in sorted(os.listdir(TEMP_IMAGE_FOLDER))],
        os.path.join(INTERFACE_VIDEO_FOLDER, f"result.{ext}")
    )


eel.init(INTERFACE_FOLDER)
eel.start(INTERFACE_START_FILE)
