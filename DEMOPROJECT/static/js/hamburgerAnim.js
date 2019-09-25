function displayWindowSize() {
    var w = document.documentElement.clientWidth;
    var toggle = document.querySelector(".toggle input");
    var menu = document.getElementById('menuPanel');

    if (w > 640) {
        toggle.checked = false;
        menu.style.cssText = ';display:block !important;'
    }
    else if (w < 640) {
        toggle.checked = false;
        menu.style.cssText = ';display:none !important;'
    }
}
window.addEventListener("resize", displayWindowSize);

var menu = document.getElementById('menuPanel');
var checkbox = document.getElementById('myCheck');
checkbox.onclick = function () {
    this.checked ?
        menu.style.cssText += ';display:block !important;' : menu.style.cssText += ';display:none !important;'
}


