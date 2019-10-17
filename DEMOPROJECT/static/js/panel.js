var close = false;
(function () {
    // Slide In Panel - by CodyHouse.co
    var panelTriggers = document.getElementsByClassName('js-cd-panel-trigger');

    var toggle = document.querySelector(".toggle input");
    $(window).scroll(function () {
        var scroll = $(window).scrollTop();
        var homeInfo1 = $('.homeInfo1');
        var toggle = document.querySelector(".toggle input");
        var text1 = $("#fixedpoint");


        //used for testing
        var x = text1.offset();
        var y = homeInfo1.offset();

        /*displays side panel*/
        for (var i = 0; i < panelTriggers.length; i++) {
            (function (i) {
                var panelClass = 'js-cd-panel-' + panelTriggers[i].getAttribute('data-panel'),
                    panel = document.getElementsByClassName(panelClass)[0];

                // open panel when clicking on trigger btn
                //need to change this to hamburger
                if ((x.top > y.top) && (toggle.checked == true)) {
                    panelTriggers[i].addEventListener('click', function (event) {
                        event.preventDefault();
                        addClass(panel, 'cd-panel--is-visible');
                        close =false;
                    });
                }

                //close panel when clicking on 'x' or outside the panel
                panel.addEventListener('click', function (event) {
                    if (hasClass(event.target, 'js-cd-close') || hasClass(event.target, panelClass)) {
                        event.preventDefault();
                        removeClass(panel, 'cd-panel--is-visible');

                    }close = true;
                });
            })(i);
        }

    });


    //class manipulations - needed if classList is not supported
    //https://jaketrent.com/post/addremove-classes-raw-javascript/
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

    (function () {
        //scrollbar class to appear if menu is longer that viewport

    })();
})();

