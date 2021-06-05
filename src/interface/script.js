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
    
    let data_type = "temperature";
    if(document.getElementById("data_options_humidity").checked){
        data_type = "humidity";
    }
    let timestamp = Math.floor(new Date(document.getElementById("timepoint_datetime").value).valueOf() / 1000)
    let location = document.getElementById("location_options").value;
    let ext = document.getElementsByName("timepoint_format");
    for(let i=0;i<ext.length;i++){
        if(ext[i].checked){
            ext = ext[i].id.split("_")[2];
            break;
        }
    }
    
    await eel.render_timepoint(data_type, timestamp, location, ext)();
    
    document.getElementById("display_timepoint").src = `data/temp/image/result.${ext}`;
    document.getElementById("timepoint_render_button").disabled = false;
    document.getElementById("timerange_render_button").disabled = false;
}

async function render_timerange(){
    await eel.render_timerange()();
    alert("done timerange");
}

async function save(){
    await eel.save()();
    alert("done saving");
}

function changeLocation(){
    let location = document.getElementById("location_options").value;
    document.getElementById("display_timepoint").src = `data/default/image/${location}.png`;
    document.getElementById("display_timerange").src = `data/default/video/${location}.mp4`;
}