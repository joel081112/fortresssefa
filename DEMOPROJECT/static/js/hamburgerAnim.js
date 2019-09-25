function displayWindowSize() {
    var w = document.documentElement.clientWidth;
    var toggle = document.querySelector(".toggle input");
    var menu = document.getElementById('menuPanel');

    if (w > 640) {
        toggle.checked = false;
        menu.style.cssText += ';display:block !important;'
    }
    //going from small to large displays menu (as wanted)
    //going back to small menu will always menu
    //need to hide it when going to small
}

window.addEventListener("resize", displayWindowSize);

var menu = document.getElementById('menuPanel');
var checkbox = document.getElementById('myCheck');
checkbox.onclick = function () {
    this.checked ?
        menu.style.cssText += ';display:block !important;' : menu.style.cssText += ';display:none !important;'
}


