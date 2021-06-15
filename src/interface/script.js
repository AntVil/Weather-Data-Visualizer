window.onload = function(){
    setup();
}

async function setup(){
    let data_downloaded = await eel.data_downloaded()();
    document.getElementById("data_downloaded").checked = data_downloaded;
    document.getElementById("page_mask").style.opacity = "0";
    document.getElementById("page_mask").style.zIndex = "-1";
}

async function download_data(){
    let popup_buttons = document.getElementsByClassName("popup_button");
    for(let i=0;i<popup_buttons.length;i++){
        popup_buttons[i].disabled = true;
    }
    let passed = await eel.download_data()();
    if(passed){
        document.getElementById("data_downloaded").checked = true;
    }else{
        alert("something went wrong!")
    }
}


async function render_timepoint(){
    document.getElementById("timepoint_render_button").disabled = true;
    document.getElementById("timerange_render_button").disabled = true;
    document.getElementById("save_button").disabled = true;
    document.getElementById("display_loader").style.opacity = 1;
    
    let data_type = "temperature";
    if(document.getElementById("data_options_humidity").checked){
        data_type = "humidity";
    }
    let date = new Date(document.getElementById("timepoint_datetime").value);
    let timestamp = Math.floor((date.getTime()) / 1000 - date.getTimezoneOffset()*60);
    let location = document.getElementById("location_options").value;
    let plot_stations = document.getElementById("station_options_visable").checked;
    let ext = document.getElementsByName("timepoint_format");
    for(let i=0;i<ext.length;i++){
        if(ext[i].checked){
            ext = ext[i].id.split("_")[2];
            break;
        }
    }
    
    await eel.render_timepoint(
        data_type,
        plot_stations,
        timestamp,
        location,
        ext
    )();
    
    document.getElementById("display_timepoint").src = `data/temp/image/result.${ext}`;
    document.getElementById("timepoint_render_button").disabled = false;
    document.getElementById("timerange_render_button").disabled = false;
    document.getElementById("save_button").disabled = false;
    document.getElementById("display_loader").style.opacity = 0;
}

async function render_timerange(){
    document.getElementById("timepoint_render_button").disabled = true;
    document.getElementById("timerange_render_button").disabled = true;
    document.getElementById("save_button").disabled = true;
    document.getElementById("display_loader").style.opacity = 1;

    let data_type = "temperature";
    if(document.getElementById("data_options_humidity").checked){
        data_type = "humidity";
    }
    let date1 = new Date(document.getElementById("timepoint_datetime_start").value);
    let date2 = new Date(document.getElementById("timepoint_datetime_end").value);
    let timestamp1 = Math.floor((date1.getTime()) / 1000 - date1.getTimezoneOffset()*60);
    let timestamp2 = Math.floor((date2.getTime()) / 1000 - date2.getTimezoneOffset()*60);
    let location = document.getElementById("location_options").value;
    let plot_stations = document.getElementById("station_options_visable").checked;
    let ext = document.getElementsByName("timerange_format");
    for(let i=0;i<ext.length;i++){
        if(ext[i].checked){
            ext = ext[i].id.split("_")[2];
            break;
        }
    }

    await eel.render_timerange(
        data_type,
        plot_stations,
        timestamp1,
        timestamp2,
        location,
        ext
    )();
    
    document.getElementById("display_timerange").src = `data/temp/video/result.${ext}`;
    document.getElementById("timepoint_render_button").disabled = false;
    document.getElementById("timerange_render_button").disabled = false;
    document.getElementById("save_button").disabled = false;
    document.getElementById("display_loader").style.opacity = 0;
}

async function save(){
    let link = document.createElement("a");
    let file;
    if(document.getElementById("time_options_timepoint").checked){
        file = document.getElementById("display_timepoint").src
    }else{
        file = document.getElementById("display_timerange").src
    }
    link.setAttribute("href", file);
    link.setAttribute("download", file.split("/").slice(-1)[0]);
    link.click();
}

function changeLocation(){
    let location = document.getElementById("location_options").value;
    document.getElementById("display_timepoint").src = `data/default/image/${location}.png`;
    document.getElementById("display_timerange").src = `data/default/video/${location}.mp4`;
}