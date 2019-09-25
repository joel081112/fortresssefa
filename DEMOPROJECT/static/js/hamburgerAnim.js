// Auto animate for demo

var toggle = document.querySelector('.toggle input')
var animate = setInterval(() => {
    toggle.checked = !toggle.checked
}, 3000)

document.querySelector('body').addEventListener('click', () => {
    clearInterval(animate);
})


function displayWindowSize() {
    var w = document.documentElement.clientWidth;
    var toggle = document.querySelector(".toggle input");

    if (w > 640) {
        toggle.checked = false;
    }
}

window.addEventListener("resize", displayWindowSize);

