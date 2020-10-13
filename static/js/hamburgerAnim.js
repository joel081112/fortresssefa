function displayWindowSize() {
    var w = document.documentElement.clientWidth;
    var toggle = document.querySelector(".toggle input");
    var menu = document.getElementById('menuPanel');

    //affects menu appearance on screen size
    if (w > 640) {
        toggle.checked = false;
        menu.style.cssText = ';display:block;'
    } else if (w < 640) {
        toggle.checked = false;
        menu.style.cssText = ';display:none;'
    }
}

window.addEventListener("resize", displayWindowSize);

var menu = document.getElementById('menuPanel');
var checkbox = document.getElementById('myCheck');
var button = document.getElementById('mobButton');

/*
button.onclick = function () {
    var text1 = $("#fixedpoint");

    //used for testing
    var x = text1.offset();
    var y = $('.homeInfo1').offset();
    alert("Top: " + x.top + " Left: " + x.left + "Menu Top " + y.top + " Left: " + y.left + this.checked);
}
*/


checkbox.onclick = function () {
    var block = $('.block');
    var text1 = $("#fixedpoint");
    var text = $(".text");

    //used for testing
    var x = text1.offset();
    var y = block.offset();
    /*y.top is currently going off block top margin*/
    var w = document.documentElement.clientWidth;
    var h = document.documentElement.clientHeight;


    //code for offset for menu display

    //drop down menu only shows when height of device greater than 860px
    //otherwise shows panel
    if ((x.top == y.top) && (this.checked == true) && (w > 399) && (h > 859)) {
        menu.style.cssText = ';display:block !important;'
    } else if ((x.top < y.top) && (this.checked == false) && (w > 399) && (h > 859)) {
        menu.style.cssText = ';display:none !important;';
    } else if ((x.top > y.top) || (w < 400) || (h < 860)) {
        var panelTriggers = document.getElementsByClassName('js-cd-panel-trigger');
        if (panelTriggers.length > 0) {

            for (var i = 0; i < panelTriggers.length; i++) {
                (function (i) {
                    var panelClass = 'js-cd-panel-' + panelTriggers[i].getAttribute('data-panel'),
                        panel = document.getElementsByClassName(panelClass)[0];
                    var toggle = document.querySelector(".toggle input");
                    // open panel when clicking on trigger btn
                    panelTriggers[i].addEventListener('click', function (event) {

                        event.preventDefault();
                        addClass(panel, 'cd-panel--is-visible');

                        toggle.checked = true;
                    });

                    //close panel when clicking on 'x' or outside the panel
                    panel.addEventListener('click', function (event) {
                        if (hasClass(event.target, 'js-cd-close') || hasClass(event.target, panelClass)) {
                            event.preventDefault();
                            removeClass(panel, 'cd-panel--is-visible');

                            toggle.checked = false;
                        }

                    });

                })(i);
            }


        }

    }
};

function hasClass(el, className) {
    if (el.classList) return el.classList.contains(className);
    else return !!el.className.match(new RegExp('(\\s|^)' + className + '(\\s|$)'));
}

function addClass(el, className) {
    if (el.classList) el.classList.add(className);
    else if (!hasClass(el, className)) el.className += " " + className;
}

function removeClass(el, className) {
    if (el.classList) el.classList.remove(className);
    else if (hasClass(el, className)) {
        var reg = new RegExp('(\\s|^)' + className + '(\\s|$)');
        el.className = el.className.replace(reg, ' ');
    }
}

//experiment
//hide menu past homeinfo1
$(function () {
    var menu = document.getElementById('menuPanel');
    var toggle = document.querySelector(".toggle input");
    var text = $(".text");
    $(window).scroll(function () {
        var scroll = $(window).scrollTop();
        var block = $('.block');
        var w = document.documentElement.clientWidth;

        //we dont want menu to show when not at top of
        if ((w < 640) && (block.offset().top > 350)) {
            menu.style.cssText = ';display:none;'
            text.hide();
            toggle.checked = false;
        }
        if( (w < 640) && (block.offset().top > 350) && (this.checked == true) && ((x.top > y.top)) ){
            addClass(panel, 'cd-panel--is-visible');
        }
    });
});


