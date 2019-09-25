function displayWindowSize() {
    var w = document.documentElement.clientWidth;
    var toggle = document.querySelector(".toggle input");

    if (w > 640) {
        toggle.checked = false;
    }
}

window.addEventListener("resize", displayWindowSize);

