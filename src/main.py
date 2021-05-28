# this file is the entry point for the project
import eel
import os
import dwd


@eel.expose
def data_downloaded():
    return dwd.dwd_downloaded()


@eel.expose
def download_data():
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
    print("render_timepoint")


@eel.expose
def render_timerange():
    print("render_timerange")


@eel.expose
def save():
    print("save")


eel.init(os.path.join(os.path.dirname(__file__), "interface"))
eel.start("index.html")
