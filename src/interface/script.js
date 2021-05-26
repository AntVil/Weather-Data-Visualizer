window.onload = function(){
    setup();
}

async function setup(){
    let data_downloaded = await eel.data_downloaded()();
    document.getElementById("data_downloaded").checked = data_downloaded;
}

async function download_data(){
    console.log("downloading data!")
    let passed = await eel.download_data()();
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