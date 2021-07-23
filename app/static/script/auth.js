function send(form, event) {
    event.preventDefault()
    url = form.action
    formData = new FormData(form)
    fetch(url, {
        method: form.method,
        body: formData,
    })
    .then(res=>getResponseToJSON(res))
    .then(json=>getJSON(json))
    .catch(err=>console.error('Error:', err));
}

function getResponseToJSON(res) {
    return res.json()
}

function getJSON(json) {
    showMsg(json.message)
    if (json.redirect) {
        setTimeout(()=>{
            location.href = json.redirect
        }
        , 2000)
    }
    console.log('Success:', json)
}
function showMsg(msg) {
    m = document.getElementById('message')
    m.innerHTML = msg
}
