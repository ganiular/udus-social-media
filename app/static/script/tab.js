var pushedState = false

function onhashchangeCallback(event){
    console.log('HashChanged:', event)
}
function onpopstateCallback(event){
    pushedState = false;
    console.log('PopState:', event)
    var tablinks, tabcontainers, i;
    tablinks = document.getElementsByClassName('tablinks')
    for(i of tablinks){
        i.classList.remove('active')
    }
    document.getElementById("tab1").classList.add('active')

    tabcontainers = document.getElementsByClassName('tabcontainers')
    for(i of tabcontainers){
        i.classList.remove('show')
    }
    document.getElementById("latest").classList.add('show')
    document.title = 'Home';
    tabblock.scrollTop = 0;
}

function changeTab(obj, target){
    var tablinks, tabcontainers, i;
    var title = target[0].toUpperCase() + target.substring(1)
    tablinks = document.getElementsByClassName('tablinks')
    for(i of tablinks){
        i.classList.remove('active')
    }
    obj.classList.add('active')

    tabcontainers = document.getElementsByClassName('tabcontainers')
    for(i of tabcontainers){
        if(i.classList.contains('show')){
            i.scrollPosition = tabblock.scrollTop || 0
            i.classList.remove('show')
        }
    }
    var tabcontainer = document.getElementById(target)
    tabcontainer.classList.add('show')
    tabblock.scrollTop = tabcontainer.scrollPosition || 0

    if(!pushedState){
        pushedState = true;
        if(location.pathname != '/home'){
            history.replaceState(null, 'Home', 'home')
        }
        history.pushState(null, title, target)
        console.log('Pushed', target)
    }
    else{
        history.replaceState(null, title, target)
        console.log('Replace', target)
    }
    document.title = title;
}

function openMenu(){
    document.getElementById('menu').style.display = 'block'
}
function closeMenu(){
    document.getElementById('menu').style.display = 'none'
} 

window.onhashchange = onhashchangeCallback
window.onpopstate = onpopstateCallback
