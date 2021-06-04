# this file is the entry point for the project
import eel
import os
import dwd
from plot import plot_map
from image_to_video import image_to_video


#constants
INTERFACE_FOLDER = os.path.join(os.path.dirname(__file__), "interface")
INTERFACE_IMAGE_FOLDER = os.path.join(INTERFACE_FOLDER, "data", "temp", "image")
INTERFACE_VIDEO_FOLDER = os.path.join(INTERFACE_FOLDER, "data", "temp", "video")
TEMP_IMAGE_FOLDER = os.join(os.path.dirname(__file__), "data", "temp", "image")
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
    returns if all data from dwd is downloaded
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
def render_timepoint():
    """
    creates an plot in "interface/data/temp/image" to be shown on the interface
    """

    print("render_timepoint")
    plot_map(INTERFACE_IMAGE_FOLDER)


@eel.expose
def render_timerange():
    """
    creates mutiple plots and fuses them to a video in "interface/data/temp/video" to be shown on the interface
    """

    print("render_timerange")

    plot_map(TEMP_IMAGE_FOLDER)

    image_to_video(
        [os.path.join(TEMP_IMAGE_FOLDER, file) for file in os.listdir(TEMP_IMAGE_FOLDER)],
        os.path.join(INTERFACE_VIDEO_FOLDER, "video.mp4")
    )


@eel.expose
def save():
    print("save")


eel.init(INTERFACE_FOLDER)
eel.start("index.html")
