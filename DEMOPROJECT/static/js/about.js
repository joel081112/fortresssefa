(function ($) {


    $(document).ready(function () {
        showStem();
        setupFade();
        setupClickToScroll();
        setupPostAnimation();
        enableScrollAbortion();

        // Trigger window.scroll, this will initiate some of the scripts
        $(window).scroll();
    });

    function showStem() {
        var stemb = $(".stem-background");
        var stem = $(".stem");
        var timeline = $(".timeline");
        var timelineot = timeline.offset().top;
        var h = document.documentElement.clientHeight;
        var timelineb =timeline.offset().top + timeline.outerHeight(true);

        $(window).scroll(function () {
            var scroll = $(window).scrollTop();
            if (scroll>timelineot-h) {
                stem.show();
                stemb.show();
                stem.height(scroll+h-timelineot);
                stem.offset({top:timelineot});
                stemb.offset({top:timelineot});
                if(scroll<timelineot){
					stemb.height(h/2+scroll-timelineot);
				}
                else if(scroll>timelineot){
                	stemb.height(h/2+scroll-timelineot);
				}
                if((scroll)>(timelineb-h/2)){
                    stemb.height(timelineb-timelineot);
                }

                if(scroll > (timelineb)){
                    stem.hide();
                    stemb.hide();
                }
                else if(scroll > (timelineb-h)){
                    stem.height(timelineb-timelineot);
                }
            }
            else {
                stemb.hide();
                stem.hide();
            }
        });
    }


    // Allow user to cancel scroll animation by manually scrolling
    function enableScrollAbortion() {
        var $viewport = $('html, body');
        $viewport.on('scroll mousedown DOMMouseScroll mousewheel keyup', function (e) {
            if (e.which > 0 || e.type === 'mousedown' || e.type === 'mousewheel') {
                $viewport.stop();
            }
        });
    }


    function setupPostAnimation() {
        var posts = $('.post-wrapper .post');
        $(window).on('scroll resize', function () {

            var currScroll = $(window).scrollTop() > $(document).scrollTop() ? $(window).scrollTop() : $(document).scrollTop(),
                windowHeight = $(window).height(), // Needs to be here because window can resize
                overScroll = Math.ceil(windowHeight * .20),
                treshhold = (currScroll + windowHeight) - overScroll;

            posts.each(function () {

                var post = $(this),
                    postScroll = post.offset().top

                if (postScroll > treshhold) {
                    post.addClass('hidden');
                } else {
                    post.removeClass('hidden');
                }

            });

        });
    }

    function setupFade() {

        var posts = $('.post-wrapper .post').reverse(),
            stemWrapper = $('.stem-wrapper'),
            halfScreen = $(window).height() / 2;

        $(window).on('scroll resize', function () {

            delay(function () {

                var currScroll = $(window).scrollTop() > $(document).scrollTop() ? $(window).scrollTop() : $(document).scrollTop(),
                    scrollSplit = currScroll + halfScreen;

                posts.removeClass('active').each(function () {

                    var post = $(this),
                        postOffset = post.offset().top;

                    if (scrollSplit > postOffset) {

                        // Add active class to fade in
                        post.addClass('active')

                        // Get post color
                        var color = post.data('stem-color') ? post.data('stem-color') : null,
                            allColors = 'color-green color-yellow color-white'

                        stemWrapper.removeClass(allColors);

                        if (color !== null) {
                            stemWrapper.addClass('color-' + color);
                        }

                        return false;
                    }

                });
            }, 20);

        });

    }


    function setupClickToScroll(post) {

        var scrollSpeed = 750;

        $('.post-wrapper .post .stem-overlay .icon').click(function (e) {
            e.preventDefault();

            var icon = $(this),
                post = icon.closest('.post'),
                postTopOffset = post.offset().top,
                postHeight = post.height(),
                halfScreen = $(window).height() / 2,
                scrollTo = postTopOffset - halfScreen + (postHeight / 2);

            $('html, body').animate({
                scrollTop: scrollTo
            }, scrollSpeed);
        });

    }

})(jQuery);


/*==========  Helpers  ==========*/


// Timeout function
var delay = (function () {
    var timer = 0;
    return function (callback, ms) {
        clearTimeout(timer);
        timer = setTimeout(callback, ms);
    };
})();

$.fn.reverse = function () {
    return this.pushStack(this.get().reverse(), arguments);
};





