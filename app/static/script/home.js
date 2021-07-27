var forumsLoaded = false
var hasGotFormData = false

function getResources(url, callback, targetElement){
    fetch(url)
    .then(response => response.json())
    .then(data => callback(data, targetElement, true))
    .catch(error => callback(error, targetElement, false))
}

function onForumShow(forumElem){
    console.log('onForumShow')
    if(!forumsLoaded){
        forumElem.classList.add('wait')
        if(!hasGotFormData){
            getResources(location.origin + '/api/forums', setForumData, forumElem)
        }
    }
}

function setForumData(data, forumElem, success){
    if(!success){
        console.error(data)
        forumElem.classList.remove('wait')
        return
    }
    var categories = null;
    var favorites = null;
    var anchors = null;
    hasGotFormData = true;
    console.log(data)
    var html = "<ul>"
    for(let i in data){
        html += `<li class="category">${i}</li><ul class="forum_lists">`
        for(let j of data[i]){
            html += `<li><a href="${location.origin + '/forums/' + j.id + '/' + j.name}">${j.name}</a><span>♥</span></li>`
        }
        html += '</ul>\n'
    }
    html += "</ul>"
    forumElem.innerHTML = html
    categories = forumElem.getElementsByClassName('category')
    for(const i of categories){
        i.addEventListener("click", function(){
            this.classList.toggle('open')
        })
    }
    favorites = forumElem.getElementsByTagName('span')
    for(const i of favorites){
        i.addEventListener('click', function(){
            // this should toggle favorites on server
            console.log("NotImplimented")
        })
    }
    anchors = forumElem.getElementsByTagName('a')
    for(let i of anchors){
        i.addEventListener("click", onForumClick)
    }
    forumElem.classList.remove('wait')
    forumsLoaded = true
}

function onForumClick(event){
    event.preventDefault()
    history.pushState({page:"forum"}, '', this.href) 
    scr = document.getElementById('screen')
    scr.classList.add('show')
}