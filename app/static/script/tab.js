var pushedState = false
var chatsLoaded = false
    

function onhashchangeCallback(event){
    console.log('HashChanged:', event)
}
function onpopstateCallback(event){
    console.log('onPopState:', event)

    if(event && event.state && event.state.page.startsWith('tab')){
        document.getElementById('screen').classList.remove('show')
        loadTab(event.state.page.substring(3))
    }
    else if(event && event.state && event.state.page == 'forum'){
        document.getElementById('screen').classList.add('show')
    }
    else{
        pushedState = false;
        loadTab('latest')
    }
}

function loadTab(target){
    var tablinks, tabcontainers, i;
    tablinks = document.getElementsByClassName('tablinks')
    for(i of tablinks){
        i.classList.remove('active')
    }
    document.getElementById("tab"+target).classList.add('active')

    tabcontainers = document.getElementsByClassName('tabcontainers')
    for(i of tabcontainers){
        if(i.classList.contains('show')){
            i.scrollPosition = tabblock.scrollTop || 0
            i.classList.remove('show')
        }
    }
    var tabcontainer = document.getElementById(target)
    tabcontainer.classList.add('show')
    if (location.pathname == '/home'){
        tabblock.scrollTop = 0
        document.title = "Home"
    }else{
        tabblock.scrollTop = tabcontainer.scrollPosition || 0
    }
    return tabcontainer
}

function changeTab(obj, target){
    var title = target[0].toUpperCase() + target.substring(1)
    var tabcontainer = loadTab(target)

    if(!pushedState){
        pushedState = true;
        if(location.pathname != '/home'){
            history.replaceState({page:"home"}, 'Home', 'home')
        }
        history.pushState({page:"tab"+target}, title, target)
        console.log('Pushed', target)
    }
    else{
        history.replaceState({page:"tab"+target}, title, target)
        console.log('Replace', target)
    }
    document.title = title;

    if(target == 'forums'){
        onForumShow(tabcontainer)
    }
}

function openMenu(){
    document.getElementById('menu').style.display = 'block'
}
function closeMenu(){
    document.getElementById('menu').style.display = 'none'
} 

window.onhashchange = onhashchangeCallback
window.onpopstate = onpopstateCallback
