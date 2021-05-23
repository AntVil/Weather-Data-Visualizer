
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