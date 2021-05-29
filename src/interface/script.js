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
    passed = true;
    if(passed){
        document.getElementById("data_downloaded").checked = true;
    }else{
        alert("something went wrong!")
    }
}


async function render_timepoint(){
    await eel.render_timepoint()();
    alert("done timepoint");
}

async function render_timerange(){
    await eel.render_timerange()();
    alert("done timerange");
}

async function save(){
    await eel.save()();
    alert("done saving");
}