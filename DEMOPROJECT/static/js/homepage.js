$(function () {
    var text = $(".text");
    $(window).scroll(function () {
        var scroll = $(window).scrollTop();

        if (scroll >= 200) {
            text.removeClass("hidden");
        } else {
            text.addClass("hidden");
        }
        if (scroll+250 > $('.homeIm2').offset().top) { // when the div with homeIm2 class scrolls into view
            text.hide();
        }
        if (scroll+250 < $('.homeIm2').offset().top) { // when the div with homeIm2 class scrolls into view
            text.show();
        }


    });
});





